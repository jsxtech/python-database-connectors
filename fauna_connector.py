"""Fauna connector using faunadb."""

import os

from faunadb import query as q
from faunadb.client import FaunaClient


def connect() -> FaunaClient:
    """Connect to Fauna.

    Environment variables:
        FAUNA_SECRET: Fauna secret key
    """
    client = FaunaClient(secret=os.environ.get('FAUNA_SECRET', '<secret-key>'))
    return client


if __name__ == "__main__":
    try:
        client = connect()
        result = client.query(q.paginate(q.databases()))
        print(f"Fauna connected. Databases: {result}")
    except Exception as e:
        print(f"Error connecting to Fauna: {e}")
