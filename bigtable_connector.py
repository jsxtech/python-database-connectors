"""Google Cloud Bigtable connector using google-cloud-bigtable."""

import os

from google.cloud import bigtable
from google.cloud.bigtable.instance import Instance


def connect() -> Instance:
    """Connect to Google Cloud Bigtable.

    Environment variables:
        BIGTABLE_PROJECT: GCP project ID
        BIGTABLE_INSTANCE: Bigtable instance ID
    """
    client = bigtable.Client(
        project=os.environ.get('BIGTABLE_PROJECT', '<project-id>'),
        admin=True
    )
    instance = client.instance(os.environ.get('BIGTABLE_INSTANCE', '<instance-id>'))
    return instance


if __name__ == "__main__":
    try:
        instance = connect()
        tables = instance.list_tables()
        print(f"Bigtable connected. Tables: {[t.table_id for t in tables]}")
    except Exception as e:
        print(f"Error connecting to Bigtable: {e}")
