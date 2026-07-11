"""Neon PostgreSQL connector using psycopg2."""

import os

import psycopg2
from psycopg2.extensions import connection


def connect() -> connection:
    """Connect to Neon PostgreSQL.

    Environment variables:
        NEON_HOST: Neon host (e.g., <project-id>.neon.tech)
        NEON_USER: Database username
        NEON_PASSWORD: Database password
        NEON_DATABASE: Database name
    """
    conn = psycopg2.connect(
        host=os.environ.get('NEON_HOST', '<project-id>.neon.tech'),
        user=os.environ.get('NEON_USER', '<username>'),
        password=os.environ.get('NEON_PASSWORD', '<password>'),
        database=os.environ.get('NEON_DATABASE', '<database>'),
        sslmode="require"
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"Neon version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to Neon: {e}")
