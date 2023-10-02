# Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the docker container
COPY requirements.txt /app/

# PIP Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Expose port 8000(Django's default is 8000)
EXPOSE 8000

# Command which Starts the Django WebApp
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
