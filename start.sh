#!/bin/bash
uvicorn --host 0.0.0.0 --port 8000 --reload --reload-exclude "./test/*.py" --reload-exclude "./test/**/*.py" --log-level info src.main:app