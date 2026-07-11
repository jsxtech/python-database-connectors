"""ArangoDB connector using python-arango."""

import os

from arango import ArangoClient
from arango.database import StandardDatabase


def connect() -> StandardDatabase:
    """Connect to ArangoDB.

    Environment variables:
        ARANGODB_HOST: ArangoDB server URL (default: http://localhost:8529)
        ARANGODB_DATABASE: Database name (default: <database>)
        ARANGODB_USERNAME: Authentication username (default: <username>)
        ARANGODB_PASSWORD: Authentication password (default: <password>)
    """
    host = os.environ.get('ARANGODB_HOST', 'http://localhost:8529')
    database = os.environ.get('ARANGODB_DATABASE', '<database>')
    username = os.environ.get('ARANGODB_USERNAME', '<username>')
    password = os.environ.get('ARANGODB_PASSWORD', '<password>')
    client = ArangoClient(hosts=host)
    db = client.db(database, username=username, password=password)
    return db


if __name__ == "__main__":
    try:
        db = connect()
        version = db.version()
        print(f"ArangoDB version: {version}")
    except Exception as e:
        print(f"Failed to connect to ArangoDB: {e}")
