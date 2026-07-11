"""Google BigQuery connector using google-cloud-bigquery."""

import os

from google.cloud import bigquery


def connect() -> bigquery.Client:
    """Connect to Google BigQuery.

    Environment variables:
        BIGQUERY_PROJECT: GCP project ID
    """
    client = bigquery.Client(project=os.environ.get('BIGQUERY_PROJECT', '<project-id>'))
    return client


if __name__ == "__main__":
    try:
        client = connect()
        query = "SELECT 1 as test"
        result = client.query(query).result()
        print(f"BigQuery connected. Test query result: {list(result)}")
    except Exception as e:
        print(f"Error connecting to BigQuery: {e}")
