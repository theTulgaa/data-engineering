# Project 6 — Orchestration (Airflow)

## Goal
Replace schedule library with Airflow. Orchestrate weather pipeline professionally.

## Architecture
Airflow DAG → fetch_weather → store_weather → Supabase

## Stack
- Apache Airflow 2.9.0
- Docker
- Python 3.12
- Pandas
- SQLAlchemy
- psycopg2
- Supabase (PostgreSQL)
- python-dotenv

## Setup
Start Docker Desktop. Then:
docker-compose up -d

Get password:
docker exec project6-airflow-1 cat /opt/airflow/standalone_admin_password.txt

Copy .env into container:
docker cp .env project6-airflow-1:/opt/airflow/.env

## Access
http://localhost:8080
Username: admin

## DAG
- dag_id: weather_pipeline
- Schedule: every 15 minutes
- Tasks: fetch_weather → store_weather
- Retries: 3 with 5 second delay

## Key Concepts Learned
- DAG = pipeline definition
- PythonOperator = run Python function as task
- XCom = pass data between tasks
- Docker = consistent environment for everyone
- Airflow replaces schedule library in production
- IPv4 pooler needed for Docker → Supabase connection
- .env must be copied into Docker container