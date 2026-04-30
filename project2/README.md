```markdown
# Project 2 — API to Database (Scheduled)

## Goal
Fetch live weather data from API every minute and store raw data into cloud PostgreSQL database automatically.

## Steps
1. Hit Open-Meteo weather API
2. Extract current weather data
3. Store raw data to Supabase with timestamp
4. Schedule to run every X minutes automatically

## Stack
- Python 3.11
- Requests
- Pandas
- SQLAlchemy
- psycopg2
- Supabase (PostgreSQL)
- python-dotenv
- schedule

## Setup
```bash
source data/bin/activate
pip install requests psycopg2-binary sqlalchemy python-dotenv schedule pandas
```

## Run
```bash
python3 src/scheduler.py
```

## Data
- Source: Open-Meteo API (Ulaanbaatar weather)
- Table: weather_raw
- New row added every 1 minute (15 min in production)

## Lessons Learned
- API calls with requests
- append vs replace in database loading
- schedule library for automation
- Scheduler must run as .py not notebook
- Log file created where terminal runs
- Real engineers use Airflow not schedule library
```