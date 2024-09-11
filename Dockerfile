# Use the official Python 3.11 image from Docker Hub
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and any required files to the container
COPY pyscript.py .

# Define the command to run the Python script
CMD ["python", "pyscript.py"]
