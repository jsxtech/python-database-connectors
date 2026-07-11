"""EdgeDB connector using edgedb-python."""

import os

import edgedb


def connect() -> edgedb.Client:
    """Connect to EdgeDB.

    Environment variables:
        EDGEDB_HOST: EdgeDB server hostname (default: localhost)
        EDGEDB_PORT: EdgeDB server port (default: 5656)
        EDGEDB_USER: Authentication username (default: <username>)
        EDGEDB_PASSWORD: Authentication password (default: <password>)
        EDGEDB_DATABASE: Database name (default: <database>)
    """
    host = os.environ.get('EDGEDB_HOST', 'localhost')
    port = int(os.environ.get('EDGEDB_PORT', '5656'))
    user = os.environ.get('EDGEDB_USER', '<username>')
    password = os.environ.get('EDGEDB_PASSWORD', '<password>')
    database = os.environ.get('EDGEDB_DATABASE', '<database>')
    client = edgedb.create_client(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        result = client.query("SELECT sys::get_version_as_str()")
        print(f"EdgeDB version: {result[0]}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to EdgeDB: {e}")
