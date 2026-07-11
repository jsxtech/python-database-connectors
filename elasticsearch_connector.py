"""Elasticsearch connector using the official elasticsearch-py client."""

import os

from elasticsearch import Elasticsearch


def connect() -> Elasticsearch:
    """Connect to Elasticsearch and return the client.

    Environment Variables:
        ES_HOST: Elasticsearch host URL (default: http://localhost:9200)
        ES_USERNAME: Authentication username
        ES_PASSWORD: Authentication password
    """
    host = os.environ.get('ES_HOST', 'http://localhost:9200')
    username = os.environ.get('ES_USERNAME', '<username>')
    password = os.environ.get('ES_PASSWORD', '<password>')

    client = Elasticsearch(
        [host],
        basic_auth=(username, password)
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        info = client.info()
        print(f"Elasticsearch version: {info['version']['number']}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Elasticsearch: {e}")
