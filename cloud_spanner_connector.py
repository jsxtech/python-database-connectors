"""Google Cloud Spanner connector using google-cloud-spanner."""

import os

from google.cloud import spanner
from google.cloud.spanner_v1.database import Database


def connect() -> Database:
    """Connect to Google Cloud Spanner.

    Environment variables:
        SPANNER_PROJECT: GCP project ID
        SPANNER_INSTANCE: Spanner instance ID
        SPANNER_DATABASE: Spanner database ID
    """
    client = spanner.Client(project=os.environ.get('SPANNER_PROJECT', '<project-id>'))
    instance = client.instance(os.environ.get('SPANNER_INSTANCE', '<instance-id>'))
    database = instance.database(os.environ.get('SPANNER_DATABASE', '<database-id>'))
    return database


if __name__ == "__main__":
    try:
        database = connect()
        with database.snapshot() as snapshot:
            results = snapshot.execute_sql("SELECT 1")
            print(f"Cloud Spanner connected. Test query: {list(results)}")
    except Exception as e:
        print(f"Error connecting to Cloud Spanner: {e}")
