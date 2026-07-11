"""OpenSearch connector using the opensearch-py client."""

import os

from opensearchpy import OpenSearch


def connect() -> OpenSearch:
    """Connect to OpenSearch and return the client.

    Environment Variables:
        OPENSEARCH_HOST: OpenSearch host (default: localhost)
        OPENSEARCH_PORT: OpenSearch port (default: 9200)
        OPENSEARCH_USERNAME: Authentication username
        OPENSEARCH_PASSWORD: Authentication password
        OPENSEARCH_USE_SSL: Whether to use SSL (default: false)
    """
    host = os.environ.get('OPENSEARCH_HOST', 'localhost')
    port = int(os.environ.get('OPENSEARCH_PORT', '9200'))
    username = os.environ.get('OPENSEARCH_USERNAME', '<username>')
    password = os.environ.get('OPENSEARCH_PASSWORD', '<password>')
    use_ssl = os.environ.get('OPENSEARCH_USE_SSL', 'false').lower() == 'true'

    client = OpenSearch(
        hosts=[{"host": host, "port": port}],
        http_auth=(username, password),
        use_ssl=use_ssl
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        info = client.info()
        print(f"OpenSearch version: {info['version']['number']}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to OpenSearch: {e}")
