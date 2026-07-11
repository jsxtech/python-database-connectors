"""YugabyteDB connector using psycopg2 (PostgreSQL-compatible)."""

import os

import psycopg2
from psycopg2.extensions import connection


def connect() -> connection:
    """Connect to YugabyteDB.

    Environment variables:
        YUGABYTEDB_HOST: YugabyteDB server hostname (default: localhost)
        YUGABYTEDB_PORT: YugabyteDB YSQL port (default: 5433)
        YUGABYTEDB_USERNAME: Authentication username (default: <username>)
        YUGABYTEDB_PASSWORD: Authentication password (default: <password>)
        YUGABYTEDB_DATABASE: Database name (default: <database>)
    """
    host = os.environ.get('YUGABYTEDB_HOST', 'localhost')
    port = int(os.environ.get('YUGABYTEDB_PORT', '5433'))
    username = os.environ.get('YUGABYTEDB_USERNAME', '<username>')
    password = os.environ.get('YUGABYTEDB_PASSWORD', '<password>')
    database = os.environ.get('YUGABYTEDB_DATABASE', '<database>')
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"YugabyteDB version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to YugabyteDB: {e}")
