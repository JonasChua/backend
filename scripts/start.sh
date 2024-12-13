#!/bin/bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir "./src" --reload-exclude "./tests/*.py" --reload-exclude "./tests/**/*.py" --log-config "./logging.conf" --log-level info 