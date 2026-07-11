"""Apache Impala connector using the impyla library."""

import os

from impala.dbapi import connect as impala_connect
from impala.hiveserver2 import HiveServer2Connection


def connect() -> HiveServer2Connection:
    """Connect to Apache Impala and return the connection.

    Returns a DB-API 2.0 compatible connection object.

    Environment Variables:
        IMPALA_HOST: Impala daemon host (default: localhost)
        IMPALA_PORT: Impala daemon port (default: 21050)
        IMPALA_DATABASE: Database name
    """
    host = os.environ.get('IMPALA_HOST', 'localhost')
    port = int(os.environ.get('IMPALA_PORT', '21050'))
    database = os.environ.get('IMPALA_DATABASE', '<database>')

    conn = impala_connect(
        host=host,
        port=port,
        database=database
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"Impala version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Impala: {e}")
