import sys
import os
from pathlib import Path

# Calculer les chemins relatifs au script
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
UTILS_DIR = PROJECT_ROOT / "airflow" / "utils"

# Ajouter le chemin des utils pour le test
sys.path.append(str(UTILS_DIR))

from reddit_extractor import RedditExtractor
from parquet_writer import write_to_parquet

def test_local_ingestion():
    print("Démarrage du test local d'extraction...")
    
    # 1. Initialisation
    user_agent = "data-market-sentiment-test/0.1"
    extractor = RedditExtractor(user_agent)
    
    # 2. Test d'extraction sur un petit échantillon
    subreddits = ["datascience"]
    print(f"Extraction de r/{subreddits[0]}...")
    df = extractor.fetch_posts(subreddits=subreddits, limit=10)
    
    if df.empty:
        print("Erreur : Le DataFrame est vide. Vérifiez votre connexion ou le User-Agent.")
        return
    
    print(f"Extraction réussie : {len(df)} posts récupérés.")
    print(df[['title', 'score']].head())

    # 3. Test d'écriture Parquet
    print("\nTest d'écriture Parquet...")
    temp_path = Path("data/tmp_test")
    temp_path.mkdir(parents=True, exist_ok=True)
    
    try:
        write_to_parquet(df, str(temp_path))
        print(f"Fichiers Parquet générés dans {temp_path}")
    except Exception as e:
        print(f"Erreur lors de l'écriture Parquet : {str(e)}")

if __name__ == "__main__":
    test_local_ingestion()
