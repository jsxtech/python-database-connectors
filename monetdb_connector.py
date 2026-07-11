"""MonetDB connector using the pymonetdb library."""

import os

import pymonetdb


def connect() -> pymonetdb.Connection:
    """Connect to MonetDB and return the connection.

    Environment Variables:
        MONETDB_HOST: MonetDB host (default: localhost)
        MONETDB_PORT: MonetDB port (default: 50000)
        MONETDB_USERNAME: Authentication username
        MONETDB_PASSWORD: Authentication password
        MONETDB_DATABASE: Database name
    """
    host = os.environ.get('MONETDB_HOST', 'localhost')
    port = int(os.environ.get('MONETDB_PORT', '50000'))
    username = os.environ.get('MONETDB_USERNAME', '<username>')
    password = os.environ.get('MONETDB_PASSWORD', '<password>')
    database = os.environ.get('MONETDB_DATABASE', '<database>')

    conn = pymonetdb.connect(
        hostname=host,
        port=port,
        username=username,
        password=password,
        database=database
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"MonetDB version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to MonetDB: {e}")
