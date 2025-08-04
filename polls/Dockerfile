# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project's code into the container
COPY . .

# Run collectstatic to gather all static files
RUN python manage.py collectstatic --no-input

# Expose the port the app runs on
EXPOSE 8000

# The command to run your app using Gunicorn
# This will be the start command for your server
CMD ["gunicorn", "instabio.wsgi", "--bind", "0.0.0.0:8000"]