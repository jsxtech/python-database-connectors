"""TiDB connector using mysql-connector-python."""

import os

import mysql.connector
from mysql.connector.connection import MySQLConnection


def connect() -> MySQLConnection:
    """Connect to TiDB Cloud.

    Environment variables:
        TIDB_HOST: TiDB host (e.g., <host>.tidbcloud.com)
        TIDB_PORT: TiDB port (default: 4000)
        TIDB_USER: Database username
        TIDB_PASSWORD: Database password
        TIDB_DATABASE: Database name
        TIDB_SSL_CA: Path to SSL CA certificate (default: /etc/ssl/cert.pem)
    """
    conn = mysql.connector.connect(
        host=os.environ.get('TIDB_HOST', '<host>.tidbcloud.com'),
        port=int(os.environ.get('TIDB_PORT', '4000')),
        user=os.environ.get('TIDB_USER', '<username>'),
        password=os.environ.get('TIDB_PASSWORD', '<password>'),
        database=os.environ.get('TIDB_DATABASE', '<database>'),
        ssl_ca=os.environ.get('TIDB_SSL_CA', '/etc/ssl/cert.pem')
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        print(f"TiDB version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to TiDB: {e}")
