#!/usr/bin/env bash
# activate virtual environment
cd /var/www/llama-api
source venv/bin/activate

# run the FastAPI backend
cd /var/www/llama/backend
exec uvicorn main:app --host 127.0.0.1 --port 8005
