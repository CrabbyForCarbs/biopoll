#!/bin/bash

# Exit on any error
set -e

# Install Python dependencies
pip install -r requirements.txt

# Run collectstatic
python manage.py collectstatic --no-input