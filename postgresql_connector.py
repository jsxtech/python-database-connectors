"""PostgreSQL database connector."""

import os

import psycopg2


def connect() -> psycopg2.extensions.connection:
    """Connect to a PostgreSQL database.

    Environment variables:
        PG_HOST: Database host (default: localhost)
        PG_PORT: Database port (default: 5432)
        PG_USER: Database username
        PG_PASSWORD: Database password
        PG_DATABASE: Database name

    Returns:
        A PostgreSQL connection object.
    """
    conn = psycopg2.connect(
        host=os.environ.get("PG_HOST", "localhost"),
        port=int(os.environ.get("PG_PORT", "5432")),
        user=os.environ.get("PG_USER", "<username>"),
        password=os.environ.get("PG_PASSWORD", "<password>"),
        database=os.environ.get("PG_DATABASE", "<database>"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"PostgreSQL version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to PostgreSQL: {e}")
