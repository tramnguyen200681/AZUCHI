#!/bin/bash
gunicorn app2:app --bind=0.0.0.0:$PORT
