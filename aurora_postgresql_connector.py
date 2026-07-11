"""Aurora PostgreSQL connector using psycopg2."""

import os

import psycopg2
from psycopg2.extensions import connection


def connect() -> connection:
    """Connect to Aurora PostgreSQL.

    Environment variables:
        AURORA_PG_HOST: Cluster endpoint (e.g., <cluster-endpoint>.rds.amazonaws.com)
        AURORA_PG_USER: Database username
        AURORA_PG_PASSWORD: Database password
        AURORA_PG_DATABASE: Database name
        AURORA_PG_PORT: Port number (default: 5432)
    """
    conn = psycopg2.connect(
        host=os.environ.get('AURORA_PG_HOST', '<cluster-endpoint>.rds.amazonaws.com'),
        user=os.environ.get('AURORA_PG_USER', '<username>'),
        password=os.environ.get('AURORA_PG_PASSWORD', '<password>'),
        database=os.environ.get('AURORA_PG_DATABASE', '<database>'),
        port=int(os.environ.get('AURORA_PG_PORT', '5432'))
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"Aurora PostgreSQL version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to Aurora PostgreSQL: {e}")
