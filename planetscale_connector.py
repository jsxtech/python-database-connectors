"""PlanetScale connector using mysql-connector-python."""

import os

import mysql.connector
from mysql.connector.connection import MySQLConnection


def connect() -> MySQLConnection:
    """Connect to PlanetScale.

    Environment variables:
        PLANETSCALE_HOST: PlanetScale host (e.g., <host>.psdb.cloud)
        PLANETSCALE_USER: Database username
        PLANETSCALE_PASSWORD: Database password
        PLANETSCALE_DATABASE: Database name
        PLANETSCALE_SSL_CA: Path to SSL CA certificate (default: /etc/ssl/cert.pem)
    """
    conn = mysql.connector.connect(
        host=os.environ.get('PLANETSCALE_HOST', '<host>.psdb.cloud'),
        user=os.environ.get('PLANETSCALE_USER', '<username>'),
        password=os.environ.get('PLANETSCALE_PASSWORD', '<password>'),
        database=os.environ.get('PLANETSCALE_DATABASE', '<database>'),
        ssl_ca=os.environ.get('PLANETSCALE_SSL_CA', '/etc/ssl/cert.pem')
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        print(f"PlanetScale version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to PlanetScale: {e}")
