"""MySQL database connector."""

import os

import mysql.connector


def connect() -> mysql.connector.MySQLConnection:
    """Connect to a MySQL database.

    Environment variables:
        MYSQL_HOST: Database host (default: localhost)
        MYSQL_PORT: Database port (default: 3306)
        MYSQL_USER: Database username
        MYSQL_PASSWORD: Database password
        MYSQL_DATABASE: Database name

    Returns:
        A MySQL connection object.
    """
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        user=os.environ.get("MYSQL_USER", "<username>"),
        password=os.environ.get("MYSQL_PASSWORD", "<password>"),
        database=os.environ.get("MYSQL_DATABASE", "<database>"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        print(f"MySQL version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to MySQL: {e}")
