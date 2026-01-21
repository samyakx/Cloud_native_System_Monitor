provider "aws" {
  region = "us-east-1" # Change to your preferred region
}

resource "aws_ecr_repository" "monitor_repo" {
  name                 = "system-monitor-repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project = "SystemMonitor"
  }
}

# Output the URL to use in Docker commands later
output "repository_url" {
  description = "The URL of the repository"
  value       = aws_ecr_repository.monitor_repo.repository_url
}
