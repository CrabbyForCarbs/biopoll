#!/bin/bash
# build_files.sh

# Use python3.12 to match the runtime in vercel.json
python3.12 -m pip install -r requirements.txt

python3.12 manage.py collectstatic --noinput
python3.12 manage.py migrate