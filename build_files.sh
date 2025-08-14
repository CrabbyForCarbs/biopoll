#!/bin/bash
# build_files.sh

# Use python3.11 to match the runtime in vercel.json
python3.11 -m pip install -r requirements.txt

python3.11 manage.py collectstatic --noinput
python3.11 manage.py migrate