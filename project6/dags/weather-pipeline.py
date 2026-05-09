from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv
import logging

load_dotenv("/opt/airflow/.env")

logger = logging.getLogger(__name__)

default_args = {
    "owner": "batman",
    "retries": 3,
    "retry_delay": timedelta(seconds=5)
}

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=47.9&longitude=106.9&current_weather=true"
    response = requests.get(url)
    data = response.json()["current_weather"]
    data["fetched_at"] = datetime.utcnow().isoformat()
    logger.info(f"Fetched: {data}")
    return data

def store_weather(**context):
    data = context["ti"].xcom_pull(task_ids="fetch_weather")
    
    DB_URL = URL.create(
    "postgresql+psycopg2",
    username="postgres.vqssaigndessrttplwib",
    password=os.getenv("SUPABASE_PASSWORD"),
    host="aws-1-ap-northeast-1.pooler.supabase.com",
    port=6543,
    database="postgres"
    )
    
    engine = create_engine(DB_URL)
    df = pd.DataFrame([data])
    df.to_sql("weather_airflow", engine, if_exists="append", index=False)
    logger.info("Stored to database")

with DAG(
    dag_id="weather_pipeline",
    default_args=default_args,
    schedule_interval="*/15 * * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    fetch = PythonOperator(
        task_id="fetch_weather",
        python_callable=fetch_weather
    )

    store = PythonOperator(
        task_id="store_weather",
        python_callable=store_weather
    )

    fetch >> store