#!/bin/bash

cd /home/tempi/Documents/tempi/backend
exec uvicorn main:app --host 0.0.0.0 --port 8000 &

cd /home/tempi/Documents/tempi/frontend
exec npm run serve &

sleep 5s
exec firefox --kiosk http://localhost:8080/dashboard &
