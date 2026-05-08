# Project 5 — Streaming Pipeline (Kafka)

## Goal
Stream real-time weather data from API through Kafka into Supabase database.

## Architecture
Weather API → Producer → Kafka → Consumer → Supabase

## Flow
1. Producer fetches weather from Open-Meteo API
2. Producer sends message to Kafka topic (weather_stream)
3. Consumer listens to topic forever
4. Consumer stores each message to Supabase instantly

## Stack
- Python 3.11
- kafka-python
- Requests
- Pandas
- SQLAlchemy
- psycopg2
- Supabase (PostgreSQL)
- Apache Kafka (Docker)
- python-dotenv

## Setup
Start Kafka:
docker run -d --name kafka -p 9092:9092 apache/kafka:3.7.0

Activate venv:
source data/bin/activate
pip install kafka-python requests pandas sqlalchemy psycopg2-binary python-dotenv

## Run
1. Run consumer.ipynb first — leave running
2. Run producer.ipynb — sends message
3. Check Supabase weather_stream_raw table

## Key Concepts Learned
- Kafka topic = channel for messages
- Producer = sends, Consumer = receives
- auto_offset_reset latest = ignore old messages
- Consumer runs forever, catches every new message
- Batch vs streaming difference
- Docker for running Kafka locally