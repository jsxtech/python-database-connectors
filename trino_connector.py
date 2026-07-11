"""Trino connector using the trino-python-client library."""

import os

import trino


def connect() -> trino.dbapi.Connection:
    """Connect to Trino and return the connection.

    Environment Variables:
        TRINO_HOST: Trino coordinator host (default: localhost)
        TRINO_PORT: Trino coordinator port (default: 8080)
        TRINO_USER: Username for authentication
        TRINO_CATALOG: Catalog name
        TRINO_SCHEMA: Schema name
    """
    host = os.environ.get('TRINO_HOST', 'localhost')
    port = int(os.environ.get('TRINO_PORT', '8080'))
    user = os.environ.get('TRINO_USER', '<username>')
    catalog = os.environ.get('TRINO_CATALOG', '<catalog>')
    schema = os.environ.get('TRINO_SCHEMA', '<schema>')

    conn = trino.dbapi.connect(
        host=host,
        port=port,
        user=user,
        catalog=catalog,
        schema=schema
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(f"Trino version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Trino: {e}")
