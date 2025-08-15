#!/bin/bash
set -e

# Install setuptools to provide the missing 'distutils' for Python 3.12+
pip3 install setuptools

# Now, install all other dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput