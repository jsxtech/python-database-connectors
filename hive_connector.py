"""Apache Hive connector using the pyhive library."""

import os

from pyhive import hive


def connect() -> hive.Connection:
    """Connect to Apache Hive and return the connection.

    Environment Variables:
        HIVE_HOST: Hive server host (default: localhost)
        HIVE_PORT: Hive server port (default: 10000)
        HIVE_USERNAME: Authentication username
        HIVE_DATABASE: Database name (default: default)
    """
    host = os.environ.get('HIVE_HOST', 'localhost')
    port = int(os.environ.get('HIVE_PORT', '10000'))
    username = os.environ.get('HIVE_USERNAME', '<username>')
    database = os.environ.get('HIVE_DATABASE', '<database>')

    conn = hive.Connection(
        host=host,
        port=port,
        username=username,
        database=database
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"Hive version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Hive: {e}")
