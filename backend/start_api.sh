#!/bin/bash
cd /var/www/llama-api/backend
exec ../venv/bin/uvicorn main:app --host 127.0.0.1 --port 8005
