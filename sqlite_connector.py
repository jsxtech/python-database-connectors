"""SQLite database connector."""

import os
import sqlite3


def connect() -> sqlite3.Connection:
    """Connect to a SQLite database.

    Environment variables:
        SQLITE_DATABASE: Path to the database file (default: <database>.db)

    Returns:
        A SQLite connection object.
    """
    conn = sqlite3.connect(
        os.environ.get("SQLITE_DATABASE", "<database>.db")
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version()")
        print(f"SQLite version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to SQLite: {e}")
