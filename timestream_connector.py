"""AWS Timestream connector using boto3 with default credential chain."""

import os

import boto3
from botocore.client import BaseClient


def connect() -> BaseClient:
    """Connect to AWS Timestream.

    Uses the boto3 default credential chain (env vars, ~/.aws/credentials, IAM roles).

    Environment variables:
        TIMESTREAM_REGION: AWS region name
    """
    client = boto3.client(
        "timestream-write",
        region_name=os.environ.get('TIMESTREAM_REGION', '<region>')
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        databases = client.list_databases()
        print(f"Timestream connected. Databases: {[db['DatabaseName'] for db in databases['Databases']]}")
    except Exception as e:
        print(f"Error connecting to Timestream: {e}")
