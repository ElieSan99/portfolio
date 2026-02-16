from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.models import Variable
from datetime import datetime, timedelta
import os
import sys

# Ajout du chemin des utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))

from reddit_extractor import RedditExtractor
from data_validator import DataValidator
from parquet_writer import write_to_parquet

# Configuration simplifiée (plus de client_id/secret)
PROJECT_ID = Variable.get("project_id", default_var="ml-ai-project-dev")
BUCKET_NAME = Variable.get("reddit_bucket_name", default_var="ml-ai-project-dev-reddit-analytics")
SUBREDDITS = ["datascience", "dataengineering", "analytics", "businessintelligence", "MachineLearning"]

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def ingest_reddit_task(**context):
    """
    Task unifiée : Extraction (Public API) -> Validation -> Parquet -> GCS.
    """
    # 1. Récupération du User-Agent (seul requis désormais)
    user_agent = Variable.get("reddit_user_agent", default_var="data-market-sentiment/0.1")
    
    # 2. Extraction via requests
    extractor = RedditExtractor(user_agent)
    df = extractor.fetch_posts(subreddits=SUBREDDITS, limit=100)
    
    if df.empty:
        print("Aucune donnée extraite.")
        return

    # 3. Validation de base
    validator = DataValidator()
    if not validator.validate_reddit_posts(df):
        # On log l'erreur mais on peut décider de continuer ou non
        print("Avertissement: Qualité des données imparfaite.")
    
    # 4. Écriture locale temporaire (Parquet partitionné)
    run_id = context['run_id']
    temp_path = f"/tmp/reddit_ingest_{run_id}"
    os.makedirs(temp_path, exist_ok=True)
    write_to_parquet(df, temp_path)
    
    # 5. Upload vers GCS Bronze
    hook = GCSHook()
    for root, dirs, files in os.walk(temp_path):
        for file in files:
            local_file = os.path.join(root, file)
            relative_path = os.path.relpath(local_file, temp_path)
            gcs_path = f"bronze/reddit/{relative_path}"
            
            hook.upload(
                bucket_name=BUCKET_NAME,
                object_name=gcs_path,
                filename=local_file
            )
            print(f"Uploaded to GCS: {gcs_path}")

with DAG(
    'reddit_ingestion_pipeline',
    default_args=default_args,
    description='Extraction Reddit (Public API) vers GCS Bronze (Parquet)',
    schedule_interval='@hourly',
    catchup=False,
    tags=['reddit', 'ingestion', 'bronze', 'composer3'],
) as dag:

    ingest_task = PythonOperator(
        task_id='extract_and_load_gcs',
        python_callable=ingest_reddit_task,
    )

    ingest_task
