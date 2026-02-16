import requests
import random
import time
import logging
from datetime import datetime, timezone
import pandas as pd

class RedditExtractor:
    """
    Extracteur Reddit utilisant l'API publique JSON (sans PRAW/OAuth).
    Inspiré des bonnes pratiques de robustesse contre le rate-limiting.
    """
    BASE_URL = "https://www.reddit.com"
    MAX_RETRIES = 5
    TIMEOUT = (10, 30)

    def __init__(self, user_agent):
        self.user_agent = user_agent
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def _get_headers(self):
        return {
            "User-Agent": self.user_agent,
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.reddit.com/",
            "Connection": "keep-alive",
        }

    def fetch_posts(self, subreddits, limit=100, timeframe="day"):
        """
        Récupère les posts récents pour une liste de subreddits.
        """
        all_posts = []
        
        for sub in subreddits:
            try:
                posts = self._fetch_subreddit_posts(sub, limit, timeframe)
                all_posts.extend(posts)
                # Petit sleep pour éviter d'être trop agressif
                time.sleep(1.0 + random.uniform(0.1, 0.7))
            except Exception as e:
                self.logger.error(f"Échec de l'extraction pour r/{sub}: {str(e)}")
        
        return pd.DataFrame(all_posts)

    def _fetch_subreddit_posts(self, subreddit, limit, timeframe):
        url = f"{self.BASE_URL}/r/{subreddit}/new.json"
        params = {"limit": limit, "t": timeframe}
        
        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                resp = self.session.get(
                    url, 
                    headers=self._get_headers(), 
                    params=params, 
                    timeout=self.TIMEOUT
                )
                
                if resp.status_code == 429:
                    wait = float(resp.headers.get("Retry-After", 2 ** attempt))
                    wait = min(wait, 60.0) + random.uniform(0, 1.0)
                    self.logger.warning(f"[429] Rate limit sur r/{subreddit}. Attente {wait:.1f}s...")
                    time.sleep(wait)
                    continue
                
                if 500 <= resp.status_code <= 599:
                    wait = min(2 ** attempt, 30.0) + random.uniform(0, 1.0)
                    time.sleep(wait)
                    continue

                resp.raise_for_status()
                data = resp.json().get("data", {}).get("children", [])
                
                return [self._normalize_post(child.get("data", {}), subreddit) for child in data]

            except (requests.Timeout, requests.ConnectionError) as e:
                wait = min(2 ** attempt, 30.0) + random.uniform(0, 1.0)
                self.logger.error(f"Erreur réseau sur r/{subreddit}: {str(e)}. Retry {attempt}/{self.MAX_RETRIES}")
                time.sleep(wait)
        
        raise RuntimeError(f"Échec définitif pour r/{subreddit} après {self.MAX_RETRIES} tentatives.")

    def _normalize_post(self, p, subreddit):
        """
        Normalise les données brutes de l'API Reddit.
        """
        title = p.get("title", "")
        selftext = p.get("selftext", "")
        return {
            "post_id": p.get("id"),
            "title": title,
            "selftext": selftext,
            "full_text": f"{title}\n\n{selftext}".strip(),
            "author": p.get("author"),
            "created_utc": p.get("created_utc"),
            "score": p.get("score"),
            "num_comments": p.get("num_comments"),
            "upvote_ratio": p.get("upvote_ratio"),
            "subreddit": subreddit,
            "url": p.get("url"),
            "permalink": p.get("permalink"),
            "collected_at": datetime.now(timezone.utc).isoformat()
        }
