"""Apache Solr connector using the pysolr client."""

import os

import pysolr


def connect() -> pysolr.Solr:
    """Connect to Apache Solr and return the client.

    Environment Variables:
        SOLR_URL: Solr base URL (default: http://localhost:8983/solr)
        SOLR_CORE: Solr core name
    """
    url = os.environ.get('SOLR_URL', 'http://localhost:8983/solr')
    core = os.environ.get('SOLR_CORE', '<core>')

    solr = pysolr.Solr(f"{url}/{core}")
    return solr


if __name__ == "__main__":
    try:
        solr = connect()
        print(f"Solr connected. Ping: {solr.ping()}")
    except Exception as e:
        print(f"Failed to connect to Solr: {e}")
