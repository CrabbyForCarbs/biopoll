#!/bin/bash

# Exit on any error
set -e

# Run database migrations
python manage.py migrate

# Run collectstatic
python manage.py collectstatic --no-input