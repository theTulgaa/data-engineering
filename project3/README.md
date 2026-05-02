# Project 3 — Reliable Pipeline

## Goal
Make project 2 pipeline bulletproof with retries and better error handling.

## What Changed from Project 2
- Added retry logic with tenacity
- Separated fetch and store into two functions
- Pipeline logs each retry attempt
- Fails gracefully without crashing scheduler

## How Retry Works
- Tries 3 times
- Waits 5 seconds between each attempt
- Logs warning before each retry
- Raises error after all attempts fail

## Stack
- Python 3.11
- Requests
- Pandas
- SQLAlchemy
- psycopg2
- Supabase (PostgreSQL)
- python-dotenv
- schedule
- tenacity

## Setup
```bash
source data/bin/activate
pip install requests psycopg2-binary sqlalchemy python-dotenv schedule pandas tenacity
```

## Run
```bash
python3 src/scheduler.py
```

## Lessons Learned
- Retry on failure with tenacity
- Separate fetch and store logic
- `logger.info` over `logging.info`
- Real pipelines must handle failure gracefully