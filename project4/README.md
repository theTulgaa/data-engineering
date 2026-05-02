# Project 4 — Raw to Mart Transform Pipeline

## Goal
Read raw weather data from database, transform it, write to clean mart table.

## Architecture
weather_raw → transform → weather_mart

## Transformations
- Wind degrees → compass direction
- Weather code → description
- fetched_at → fetched_date + fetched_time
- Dropped: interval, fetched_at
- Reordered columns

## Stack
- Python 3.11
- Pandas
- SQLAlchemy
- psycopg2
- Supabase (PostgreSQL)
- python-dotenv

## Setup
source data/bin/activate
pip install pandas sqlalchemy psycopg2-binary python-dotenv

## Run
Open src/transform.ipynb and run all cells.

## Lessons Learned
- Raw layer = never touch original data
- Mart layer = business ready
- if_exists replace vs append
- Always read from raw, write to mart