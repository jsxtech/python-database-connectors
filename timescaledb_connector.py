"""TimescaleDB connector using psycopg2 (PostgreSQL with TimescaleDB extension)."""

import os

import psycopg2


def connect() -> psycopg2.extensions.connection:
    """Connect to TimescaleDB and return the connection.

    Environment Variables:
        TIMESCALEDB_HOST: Database host (default: localhost)
        TIMESCALEDB_PORT: Database port (default: 5432)
        TIMESCALEDB_USER: Database username
        TIMESCALEDB_PASSWORD: Database password
        TIMESCALEDB_DATABASE: Database name
    """
    host = os.environ.get('TIMESCALEDB_HOST', 'localhost')
    port = int(os.environ.get('TIMESCALEDB_PORT', '5432'))
    user = os.environ.get('TIMESCALEDB_USER', '<username>')
    password = os.environ.get('TIMESCALEDB_PASSWORD', '<password>')
    database = os.environ.get('TIMESCALEDB_DATABASE', '<database>')

    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT extversion FROM pg_extension WHERE extname = 'timescaledb'")
        print(f"TimescaleDB version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to TimescaleDB: {e}")
