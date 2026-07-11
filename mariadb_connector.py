"""MariaDB database connector."""

import os

import mariadb


def connect() -> mariadb.Connection:
    """Connect to a MariaDB database.

    Environment variables:
        MARIADB_HOST: Database host (default: localhost)
        MARIADB_PORT: Database port (default: 3306)
        MARIADB_USER: Database username
        MARIADB_PASSWORD: Database password
        MARIADB_DATABASE: Database name

    Returns:
        A MariaDB connection object.
    """
    conn = mariadb.connect(
        host=os.environ.get("MARIADB_HOST", "localhost"),
        port=int(os.environ.get("MARIADB_PORT", "3306")),
        user=os.environ.get("MARIADB_USER", "<username>"),
        password=os.environ.get("MARIADB_PASSWORD", "<password>"),
        database=os.environ.get("MARIADB_DATABASE", "<database>"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        print(f"MariaDB version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to MariaDB: {e}")
