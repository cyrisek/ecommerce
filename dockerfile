# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Start Gunicorn with the appropriate settings
CMD ["gunicorn", "ecommerce.wsgi:application", "--bind", "0.0.0.0:8000"]