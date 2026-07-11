"""DuckDB database connector."""

import os

import duckdb


def connect() -> duckdb.DuckDBPyConnection:
    """Connect to a DuckDB database.

    Environment variables:
        DUCKDB_DATABASE: Path to the database file (default: <database>.db)

    Returns:
        A DuckDB connection object.
    """
    conn = duckdb.connect(
        database=os.environ.get("DUCKDB_DATABASE", "<database>.db")
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        result = conn.execute("SELECT version()").fetchone()
        print(f"DuckDB version: {result[0]}")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to DuckDB: {e}")
