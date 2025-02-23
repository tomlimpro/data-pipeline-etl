# Import DAG clsss
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta

def afficher_message():
    print("Hello world :)")

# défintion des arguments par défaut du DAG

default_args = {
    "owner": "admin",
    "depends_on_past": False,
    "start_date": datetime(2024,2,22),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# Creation du DAG

with DAG(
    dag_id="my_first_dag_test",
    default_args = default_args,
    description="Un DAG simple pour débuter",
    schedule_interval= timedelta(days=1),
    catchup=False
) as dag:

    # Défintion d'une tache utilisant PythonOperator
    tache_hello = PythonOperator(
        task_id = "afficher_message",
        python_callable=afficher_message
    )



