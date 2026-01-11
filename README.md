# Project README

## 1. Dependencies and Requirements
* **Python Version:** 3.11
* **Installation:**
```bash
pip install -r requirements.txt
```

## 2. Docker Deployment
To build and start the application containers in the background, use:

```bash
docker-compose up -d --build
```
### Database Initialization (init.sql)
The init.sql script runs automatically when the database container is first created. It defines the schema and initial data.

**How to expand the database**: To add more records, append sequential INSERT INTO queries to the init.sql file. This ensures the data is populated during the initialization phase.

```SQL
-- Example of sequential inserts
INSERT INTO users (name, email) VALUES ('User 1', 'user1@example.com');
INSERT INTO users (name, email) VALUES ('User 2', 'user2@example.com');
```
Note: If the database has already been initialized, you must run docker-compose down -v to remove the existing volume before the updated script will run again.

## 3. Running with Uvicorn
For local development and debugging without Docker, run the application directly using Uvicorn:

```bash
uvicorn main:app --reload
```
main:app: Refers to the app instance located in main.py.

--reload: Enables automatic server restarts upon code changes.
