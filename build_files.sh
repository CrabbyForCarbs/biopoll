#!/bin/bash
set -e

# Upgrade packaging tools to be compatible with Python 3.12
pip3 install --upgrade pip setuptools

# Now, install all other dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput