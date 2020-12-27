#!/bin/bash

if [ "$1" = "record" ]; then
    python -m src.av.recorder
elif [ "$1" = "serve" ]; then
    gunicorn --workers 1 --bind 0.0.0.0:8080 app:app --threads 2 --worker-class gevent
    # flask run --host 0.0.0.0 --port 8080
fi
