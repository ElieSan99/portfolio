from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.operators.functions import CloudFunctionInvokeFunctionOperator

default_args = {
    'owner': 'Elie Sanon',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'twitter_sentiment_etl',
    default_args=default_args,
    description='Pipeline ETL pour l\'analyse de sentiment Twitter',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['GCP', 'Twitter', 'Sentiment'],
) as dag:

    trigger_ingestion = CloudFunctionInvokeFunctionOperator(
        task_id='trigger_twitter_ingestion',
        function_id='fetch-tweets-function',
        location='europe-west1',
    )

    sentiment_processing = BigQueryExecuteQueryOperator(
        task_id='run_sentiment_analysis',
        sql='bigquery/sentiment_analysis.sql',
        use_legacy_sql=False,
        destination_dataset_table='portfolio_gold.twitter_sentiment_stats',
        write_disposition='WRITE_APPEND',
    )

    trigger_ingestion >> sentiment_processing
