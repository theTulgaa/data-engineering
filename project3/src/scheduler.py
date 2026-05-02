from tenacity import before_sleep_log
import schedule
import time
import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv
import logging
from tenacity import retry, stop_after_attempt, wait_fixed

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

load_dotenv("../.env")

DB_URL = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password=os.getenv("SUPABASE_PASSWORD"),
    host="db.vqssaigndessrttplwib.supabase.co",
    port=5432,
    database="postgres"
)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(5),
    before_sleep=before_sleep_log(logger, logging.WARNING)
)
def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=47.9&longitude=106.9&current_weather=true"
    response = requests.get(url)
    data = response.json()["current_weather"]
    data["fetched_at"] = datetime.utcnow()
    return data

def store_weather(data):
    try:
        df = pd.DataFrame([data])
        engine = create_engine(DB_URL)
        df.to_sql("weather_raw", engine, if_exists="append", index=False)
        logger.info(f"Stored weather data at {data['fetched_at']}")
    except Exception as e:
        logger.error(f"DB error: {e}")
        raise

def run_pipeline():
    try:
        data = fetch_weather()
        store_weather(data)
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")

schedule.every(1).minutes.do(run_pipeline)
logger.info("Scheduler started")
run_pipeline()

while True:
    schedule.run_pending()
    time.sleep(60)