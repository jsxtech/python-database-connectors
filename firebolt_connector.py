"""Firebolt connector using firebolt-sdk."""

import os

from firebolt.db import connect as firebolt_connect
from firebolt.db.connection import Connection


def connect() -> Connection:
    """Connect to Firebolt.

    Environment variables:
        FIREBOLT_ENGINE: Engine name
        FIREBOLT_DATABASE: Database name
        FIREBOLT_USERNAME: Username
        FIREBOLT_PASSWORD: Password
    """
    conn = firebolt_connect(
        engine_name=os.environ.get('FIREBOLT_ENGINE', '<engine>'),
        database=os.environ.get('FIREBOLT_DATABASE', '<database>'),
        username=os.environ.get('FIREBOLT_USERNAME', '<username>'),
        password=os.environ.get('FIREBOLT_PASSWORD', '<password>')
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"Firebolt version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to Firebolt: {e}")
