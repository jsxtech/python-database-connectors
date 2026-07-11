"""Google AlloyDB connector using psycopg2."""

import os

import psycopg2
from psycopg2.extensions import connection


def connect() -> connection:
    """Connect to Google AlloyDB.

    Environment variables:
        ALLOYDB_HOST: AlloyDB instance IP address
        ALLOYDB_USER: Database username
        ALLOYDB_PASSWORD: Database password
        ALLOYDB_DATABASE: Database name
        ALLOYDB_PORT: Port number (default: 5432)
    """
    conn = psycopg2.connect(
        host=os.environ.get('ALLOYDB_HOST', '<alloydb-instance-ip>'),
        user=os.environ.get('ALLOYDB_USER', '<username>'),
        password=os.environ.get('ALLOYDB_PASSWORD', '<password>'),
        database=os.environ.get('ALLOYDB_DATABASE', '<database>'),
        port=int(os.environ.get('ALLOYDB_PORT', '5432'))
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"AlloyDB version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to AlloyDB: {e}")
