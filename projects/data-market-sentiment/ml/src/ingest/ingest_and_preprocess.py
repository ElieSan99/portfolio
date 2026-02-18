import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv
from tqdm import tqdm
from google.cloud import storage

load_dotenv()

USER_AGENT = os.getenv("REDDIT_USER_AGENT", "data-market-sentiment/0.1 by yourname")
BASE_URL = "https://www.reddit.com"

# ⚠️ À ADAPTER : bucket DEV
GCS_BUCKET = os.getenv("GCS_BUCKET", "dms-raw-dev")


def fetch_new_posts(subreddit: str, limit: int = 100) -> list[dict]:
    """
    Récupère les posts récents d'un subreddit via l'endpoint public JSON de Reddit.
    """
    url = f"{BASE_URL}/r/{subreddit}/new.json?limit={limit}"
    headers = {"User-Agent": USER_AGENT}

    # timeout=(connect, read) : évite de rester bloqué trop longtemps
    response = requests.get(url, headers=headers, timeout=(10, 30))
    response.raise_for_status()

    payload = response.json()
    children = payload.get("data", {}).get("children", [])

    posts = [
        child.get("data", {})
        for child in children
        if isinstance(child, dict)
    ]
    return posts


def to_clean_record(p: dict, subreddit: str) -> dict:
    """
    Normalise un post Reddit brut en enregistrement stable (raw table friendly).
    """
    post_id = p.get("id") or p.get("name")
    title = p.get("title") or ""
    selftext = p.get("selftext") or ""
    full_text = (title + "\n\n" + selftext).strip()

    return {
        "source": "reddit",
        "subreddit": subreddit,
        "collected_at": datetime.now(timezone.utc).isoformat(),  # ISO UTC
        "post_id": post_id,
        "created_utc": p.get("created_utc") or p.get("created"),
        "title": title,
        "selftext": selftext,
        "full_text": full_text,
        "author": p.get("author"),
        "permalink": p.get("permalink"),
        "url": p.get("url"),
        "score": p.get("score"),
        "num_comments": p.get("num_comments"),
        "upvote_ratio": p.get("upvote_ratio"),
        "over_18": p.get("over_18"),
    }


def write_jsonl_overwrite(out_path: Path, records: list[dict]) -> None:
    """
    Écrit un fichier JSONL en mode overwrite (write).
    Important: on évite 'append' pour ne pas mélanger plusieurs runs dans le même fichier.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def upload_to_gcs(bucket_name: str, local_path: Path, gcs_path: str) -> str:
    """
    Upload un fichier local vers GCS. Retourne l'URI gs://...
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(str(local_path))
    return f"gs://{bucket_name}/{gcs_path}"


def main():
    subreddits = [
        "datascience",
        "dataengineering",
        "analytics",
        "businessintelligence",
    ]
    limit = 50

    run_ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # on utilise un dossier temporaire local (fiable Windows), puis upload vers GCS
    tmp_dir = Path("data/tmp")
    tmp_dir.mkdir(parents=True, exist_ok=True)

    total_records = 0

    for sub in tqdm(subreddits, desc="Subreddits"):
        time.sleep(1.2)  # rate limit friendly

        posts = fetch_new_posts(sub, limit=limit)

        # pas d'idempotence : on prend tout ce que l'API renvoie à chaque run
        records = [to_clean_record(p, subreddit=sub) for p in posts if (p.get("id") or p.get("name"))]

        tmp_path = tmp_dir / f"reddit_{sub}_{run_ts}.jsonl"
        write_jsonl_overwrite(tmp_path, records)

        gcs_path = f"raw/reddit/{run_ts}/{tmp_path.name}"
        gcs_uri = upload_to_gcs(GCS_BUCKET, tmp_path, gcs_path)

        print(f"[{sub}] fetched={len(posts)} wrote={len(records)} -> {gcs_uri}")
        total_records += len(records)

    print(f"Fait. Total records uploadés: {total_records}")


if __name__ == "__main__":
    main()
