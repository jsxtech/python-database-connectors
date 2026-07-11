"""Stardog RDF database connector using the pystardog library."""

import os

from stardog import Connection


def connect() -> Connection:
    """Connect to Stardog and return the connection.

    Environment Variables:
        STARDOG_ENDPOINT: Stardog server endpoint (default: http://localhost:5820)
        STARDOG_DATABASE: Database name (default: stardog)
        STARDOG_USERNAME: Authentication username
        STARDOG_PASSWORD: Authentication password
    """
    endpoint = os.environ.get('STARDOG_ENDPOINT', 'http://localhost:5820')
    database = os.environ.get('STARDOG_DATABASE', 'stardog')
    username = os.environ.get('STARDOG_USERNAME', '<username>')
    password = os.environ.get('STARDOG_PASSWORD', '<password>')

    conn = Connection(
        database,
        endpoint=endpoint,
        username=username,
        password=password
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        result = conn.select("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
        print(f"Stardog connected. Result: {result}")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Stardog: {e}")
