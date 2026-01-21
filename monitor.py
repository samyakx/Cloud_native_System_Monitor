import psutil
import time
import boto3
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ecr_connectivity(repo_name):
    """
    Uses Boto3 to check if the ECR repository exists and is accessible.
    """
    try:
        # Ensure your container has AWS credentials (via env vars or IAM role)
        client = boto3.client('ecr', region_name='us-east-1') 
        response = client.describe_repositories(repositoryNames=[repo_name])
        repo_uri = response['repositories'][0]['repositoryUri']
        logging.info(f"✅ Connected to AWS ECR: {repo_uri}")
    except Exception as e:
        logging.error(f"❌ Failed to connect to ECR: {e}")

def monitor_system():
    """
    Logs basic system stats.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    
    logging.info(f"System Stats - CPU: {cpu_usage}% | RAM: {memory_info.percent}%")

if __name__ == "__main__":
    REPO_NAME = os.getenv("REPO_NAME", "system-monitor-repo")
    
    logging.info("Starting System Monitor...")
    
    # Check ECR connection once on startup
    check_ecr_connectivity(REPO_NAME)
    
    try:
        while True:
            monitor_system()
            time.sleep(5)
    except KeyboardInterrupt:
        logging.info("Stopping Monitor.")
