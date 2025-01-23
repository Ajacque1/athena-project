# Use the official Python 3 image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements and Python script into the container
COPY requirements.txt .
COPY query_athena.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the script
CMD ["python", "query_athena.py"]
