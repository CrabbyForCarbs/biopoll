#!/bin/bash
# build_files.sh

# Use the generic 'python' command
python -m pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate