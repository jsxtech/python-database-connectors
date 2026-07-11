"""Presto connector using the prestodb library."""

import os

import prestodb


def connect() -> prestodb.dbapi.Connection:
    """Connect to Presto and return the connection.

    Environment Variables:
        PRESTO_HOST: Presto coordinator host (default: localhost)
        PRESTO_PORT: Presto coordinator port (default: 8080)
        PRESTO_USER: Username for authentication
        PRESTO_CATALOG: Catalog name
        PRESTO_SCHEMA: Schema name
    """
    host = os.environ.get('PRESTO_HOST', 'localhost')
    port = int(os.environ.get('PRESTO_PORT', '8080'))
    user = os.environ.get('PRESTO_USER', '<username>')
    catalog = os.environ.get('PRESTO_CATALOG', '<catalog>')
    schema = os.environ.get('PRESTO_SCHEMA', '<schema>')

    conn = prestodb.dbapi.connect(
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
        print(f"Presto version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Presto: {e}")
