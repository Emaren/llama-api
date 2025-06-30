#!/usr/bin/env bash
# cd into backend/ so “routes” is on the module path
cd /var/www/llama/backend
exec uvicorn main:app --host 0.0.0.0 --port 8003
