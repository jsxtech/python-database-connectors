"""AWS DynamoDB connector using boto3 with default credential chain."""

import os

import boto3
from boto3.resources.base import ServiceResource


def connect() -> ServiceResource:
    """Connect to AWS DynamoDB.

    Uses the boto3 default credential chain (env vars, ~/.aws/credentials, IAM roles).

    Environment variables:
        DYNAMODB_REGION: AWS region name
    """
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=os.environ.get('DYNAMODB_REGION', '<region>')
    )
    return dynamodb


if __name__ == "__main__":
    try:
        dynamodb = connect()
        tables = list(dynamodb.tables.all())
        print(f"DynamoDB connected. Tables: {[t.name for t in tables]}")
    except Exception as e:
        print(f"Error connecting to DynamoDB: {e}")
