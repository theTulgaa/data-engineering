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

def fetch_and_store():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=47.9&longitude=106.9&current_weather=true"
        response = requests.get(url)
        data = response.json()["current_weather"]
        data["fetched_at"] = datetime.utcnow()
        df = pd.DataFrame([data])
        engine = create_engine(DB_URL)
        df.to_sql("weather_raw", engine, if_exists="append", index=False)
        logger.info(f"Stored weather data at {data['fetched_at']}")
    except Exception as e:
        logger.error(f"Error: {e}")

schedule.every(1).minutes.do(fetch_and_store)

logger.info("Scheduler started")
fetch_and_store()

while True:
    schedule.run_pending()
    time.sleep(60)