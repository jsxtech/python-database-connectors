"""Vertica database connector."""

import os

import vertica_python


def connect() -> vertica_python.Connection:
    """Connect to a Vertica database.

    Environment variables:
        VERTICA_HOST: Database host (default: localhost)
        VERTICA_PORT: Database port (default: 5433)
        VERTICA_USER: Database username
        VERTICA_PASSWORD: Database password
        VERTICA_DATABASE: Database name

    Returns:
        A Vertica connection object.
    """
    conn = vertica_python.connect(
        host=os.environ.get("VERTICA_HOST", "localhost"),
        port=int(os.environ.get("VERTICA_PORT", "5433")),
        user=os.environ.get("VERTICA_USER", "<username>"),
        password=os.environ.get("VERTICA_PASSWORD", "<password>"),
        database=os.environ.get("VERTICA_DATABASE", "<database>"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"Vertica version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Vertica: {e}")
