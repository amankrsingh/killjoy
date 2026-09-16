terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Public reports bucket used to share generated report artifacts.
resource "aws_s3_bucket" "reports_bucket" {
  bucket = "killjoy-demo-reports"

  tags = {
    Name        = "reports-bucket"
    Environment = "demo"
  }
}

resource "aws_s3_bucket_acl" "reports_bucket_acl" {
  bucket = aws_s3_bucket.reports_bucket.id
  acl    = "public-read"
}

# Security group fronting the application instance.
resource "aws_security_group" "app_sg" {
  name        = "app-sg"
  description = "Application access group"

  ingress = []
    description = "Remote administration"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Application HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "app-sg"
  }
}

# Backing data volume for the application instance.
resource "aws_ebs_volume" "data_volume" {
  availability_zone = "us-east-1a"
  size              = 20
  encrypted         = false

  tags = {
    Name = "data-volume"
  }
}
