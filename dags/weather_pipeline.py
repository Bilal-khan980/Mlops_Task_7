from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def collect_data():
    os.system("python data_collection.py")

def preprocess_data():
    os.system("python data_preprocessing.py")

with DAG(
    "weather_pipeline",
    default_args={"start_date": datetime(2024, 1, 1)},
    schedule_interval="@daily",
) as dag:
    collect = PythonOperator(task_id="collect_data", python_callable=collect_data)
    preprocess = PythonOperator(task_id="preprocess_data", python_callable=preprocess_data)

    collect >> preprocess
