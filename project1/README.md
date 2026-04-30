# Project 1 — CSV to Database

## Goal
Load, clean, and store HR attrition data into a cloud PostgreSQL database.

## Steps
1. Load CSV using pandas
2. Drop useless columns (Over18, StandardHours, EmployeeCount)
3. Standardize text columns to lowercase
4. Rename columns to snake_case
5. Load cleaned data to Supabase PostgreSQL

## Stack
- Python 3.11
- Pandas
- SQLAlchemy
- psycopg2
- Supabase (PostgreSQL)
- python-dotenv

## Setup
```bash
source data/bin/activate
pip install pandas sqlalchemy psycopg2-binary python-dotenv
```

## Run
Open `src/load.ipynb` and run all cells.

## Data
- Source: HR Attrition dataset
- Rows: 1470
- Columns: 35 (32 after cleaning)

## Lessons Learned
- Relative paths over absolute
- Logger over print
- Environment variables for secrets
- SQLAlchemy URL.create for special characters in password