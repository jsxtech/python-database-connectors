"""Couchbase connector using couchbase SDK."""

import os

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator


def connect() -> Cluster:
    """Connect to Couchbase.

    Environment variables:
        COUCHBASE_HOST: Couchbase server hostname (default: localhost)
        COUCHBASE_USERNAME: Authentication username
        COUCHBASE_PASSWORD: Authentication password
        COUCHBASE_BUCKET: Bucket name (used in example)
    """
    host = os.environ.get('COUCHBASE_HOST', 'localhost')
    username = os.environ.get('COUCHBASE_USERNAME', '<username>')
    password = os.environ.get('COUCHBASE_PASSWORD', '<password>')
    auth = PasswordAuthenticator(username, password)
    cluster = Cluster(f"couchbase://{host}", authenticator=auth)
    return cluster


if __name__ == "__main__":
    try:
        cluster = connect()
        bucket_name = os.environ.get('COUCHBASE_BUCKET', '<bucket>')
        bucket = cluster.bucket(bucket_name)
        print(f"Couchbase connected. Bucket: {bucket.name}")
    except Exception as e:
        print(f"Failed to connect to Couchbase: {e}")
