# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY monitor.py .

# Set environment variable for the repo name (optional, defaults in script)
ENV REPO_NAME="system-monitor-repo"

# Run the application
CMD ["python", "monitor.py"]
