"""rqlite connector using HTTP API via requests."""

import os

import requests


def connect() -> str:
    """Connect to rqlite and return the base URL.

    Environment variables:
        RQLITE_HOST: rqlite server hostname (default: localhost)
        RQLITE_PORT: rqlite HTTP port (default: 4001)
    """
    host = os.environ.get('RQLITE_HOST', 'localhost')
    port = os.environ.get('RQLITE_PORT', '4001')
    return f"http://{host}:{port}"


def query(url: str, sql: str) -> dict:
    """Execute a SQL query against rqlite."""
    response = requests.post(f"{url}/db/query", json=[[sql]])
    return response.json()


if __name__ == "__main__":
    try:
        url = connect()
        result = query(url, "SELECT 1")
        print(f"rqlite connected. Result: {result}")
    except Exception as e:
        print(f"Failed to connect to rqlite: {e}")
