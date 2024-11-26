# Use official Python image from Docker Hub
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the current directory content into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

# Define environment variable to ensure Python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1

# Run the Flask app
CMD ["python", "app.py"]
