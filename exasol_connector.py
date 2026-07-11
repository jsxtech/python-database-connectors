"""Exasol connector using the pyexasol library."""

import os

import pyexasol


def connect() -> pyexasol.ExaConnection:
    """Connect to Exasol and return the connection.

    Environment Variables:
        EXASOL_HOST: Exasol host (default: localhost)
        EXASOL_PORT: Exasol port (default: 8563)
        EXASOL_USER: Authentication username
        EXASOL_PASSWORD: Authentication password
    """
    host = os.environ.get('EXASOL_HOST', '<host>')
    port = os.environ.get('EXASOL_PORT', '8563')
    user = os.environ.get('EXASOL_USER', '<username>')
    password = os.environ.get('EXASOL_PASSWORD', '<password>')

    conn = pyexasol.connect(
        dsn=f"{host}:{port}",
        user=user,
        password=password
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.execute("SELECT PARAM_VALUE FROM EXA_METADATA WHERE PARAM_NAME='databaseProductVersion'")
        print(f"Exasol version: {cursor.fetchone()[0]}")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Exasol: {e}")
