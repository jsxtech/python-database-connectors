"""CockroachDB database connector."""

import os

import psycopg2


def connect() -> psycopg2.extensions.connection:
    """Connect to a CockroachDB database.

    Environment variables:
        COCKROACHDB_HOST: Database host
        COCKROACHDB_PORT: Database port (default: 26257)
        COCKROACHDB_USER: Database username
        COCKROACHDB_PASSWORD: Database password
        COCKROACHDB_DATABASE: Database name
        COCKROACHDB_SSLMODE: SSL mode (default: require)

    Returns:
        A CockroachDB connection object.
    """
    conn = psycopg2.connect(
        host=os.environ.get("COCKROACHDB_HOST", "<host>"),
        port=int(os.environ.get("COCKROACHDB_PORT", "26257")),
        user=os.environ.get("COCKROACHDB_USER", "<username>"),
        password=os.environ.get("COCKROACHDB_PASSWORD", "<password>"),
        database=os.environ.get("COCKROACHDB_DATABASE", "<database>"),
        sslmode=os.environ.get("COCKROACHDB_SSLMODE", "require"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"CockroachDB version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to CockroachDB: {e}")
