from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

# Configuration
DBT_PROJECT_DIR = "/opt/airflow/dbt_reddit_analytics"
DBT_PROFILES_DIR = DBT_PROJECT_DIR
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")

default_args = {
    "owner": "analytics_engineer",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "dbt_transformation_pipeline",
    default_args=default_args,
    description="Pipeline de transformation dbt (Medallion Architecture)",
    schedule_interval="0 2 * * *",  # Quotidien à 02:00
    catchup=False,
    tags=["dbt", "analytics", "medallion"],
) as dag:

    # 1. Mise à jour des dépendances dbt
    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt deps",
    )

    # 2. Run Silver Layer (Incremental)
    dbt_run_silver = BashOperator(
        task_id="dbt_run_silver",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run --select silver.*",
    )

    # 3. Test Silver Layer
    dbt_test_silver = BashOperator(
        task_id="dbt_test_silver",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt test --select silver.*",
    )

    # 4. Run Gold Layer
    dbt_run_gold = BashOperator(
        task_id="dbt_run_gold",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run --select gold.* marts.*",
    )

    # 5. Test Gold Layer
    dbt_test_gold = BashOperator(
        task_id="dbt_test_gold",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt test --select gold.* marts.*",
    )

    # 6. Documentation Generate
    dbt_docs = BashOperator(
        task_id="dbt_docs_generate",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt docs generate",
    )

    (
        dbt_deps
        >> dbt_run_silver
        >> dbt_test_silver
        >> dbt_run_gold
        >> dbt_test_gold
        >> dbt_docs
    )

# DAG pour le Full Refresh hebdomadaire
with DAG(
    "dbt_full_refresh_weekly",
    default_args=default_args,
    description="Full Refresh dbt (Dimanche 3h)",
    schedule_interval="0 3 * * 0",
    catchup=False,
    tags=["dbt", "admin", "full-refresh"],
) as dag_admin:

    dbt_full_run = BashOperator(
        task_id="dbt_full_refresh",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run --full-refresh",
    )
