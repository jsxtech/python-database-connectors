"""Turso connector using requests."""

import os

import requests


def connect() -> dict:
    """Connect to Turso and return configuration dict.

    Environment variables:
        TURSO_URL: Turso database URL (e.g., https://<database>.turso.io)
        TURSO_TOKEN: Authentication token
    """
    return {
        "url": os.environ.get('TURSO_URL', 'https://<database>.turso.io'),
        "token": os.environ.get('TURSO_TOKEN', '<auth-token>')
    }


def query(config: dict, sql: str) -> dict:
    """Execute a SQL query against Turso."""
    headers = {"Authorization": f"Bearer {config['token']}"}
    response = requests.post(config["url"], headers=headers, json={"statements": [sql]})
    return response.json()


if __name__ == "__main__":
    try:
        config = connect()
        result = query(config, "SELECT 1")
        print(f"Turso connected. Result: {result}")
    except Exception as e:
        print(f"Error connecting to Turso: {e}")
