"""OrientDB connector using pyorient."""

import os

import pyorient


def connect() -> pyorient.OrientDB:
    """Connect to OrientDB.

    Environment variables:
        ORIENTDB_HOST: OrientDB server hostname (default: localhost)
        ORIENTDB_PORT: OrientDB binary port (default: 2424)
        ORIENTDB_USERNAME: Authentication username
        ORIENTDB_PASSWORD: Authentication password
        ORIENTDB_DATABASE: Database name
    """
    host = os.environ.get("ORIENTDB_HOST", "localhost")
    port = int(os.environ.get("ORIENTDB_PORT", "2424"))
    username = os.environ.get("ORIENTDB_USERNAME", "<username>")
    password = os.environ.get("ORIENTDB_PASSWORD", "<password>")
    database = os.environ.get("ORIENTDB_DATABASE", "<database>")

    client = pyorient.OrientDB(host, port)
    client.connect(username, password)
    client.db_open(database, username, password)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        print(f"OrientDB connected. Client: {client}")
        client.db_close()
    except Exception as e:
        print(f"Failed to connect to OrientDB: {e}")
