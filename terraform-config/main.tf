provider "aws" {
  region = "us-east-1" # Use East Region
}

resource "aws_s3_bucket" "athena_results" {
  bucket = "test-data-project-athena-results"
  acl    = "private"

  tags = {
    Name        = "Athena Results Bucket"
    Environment = "Test"
  }
}
