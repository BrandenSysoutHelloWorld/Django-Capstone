# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables (customize as needed)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Expose the port your application will run on (Django's default is 8000)
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
