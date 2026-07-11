"""RethinkDB connector using rethinkdb Python driver."""

import os

from rethinkdb import RethinkDB
from rethinkdb.net import Connection


def connect() -> Connection:
    """Connect to RethinkDB.

    Environment variables:
        RETHINKDB_HOST: RethinkDB server hostname (default: localhost)
        RETHINKDB_PORT: RethinkDB driver port (default: 28015)
        RETHINKDB_DATABASE: Database name (default: <database>)
        RETHINKDB_USERNAME: Authentication username (default: <username>)
        RETHINKDB_PASSWORD: Authentication password (default: <password>)
    """
    r = RethinkDB()
    host = os.environ.get('RETHINKDB_HOST', 'localhost')
    port = int(os.environ.get('RETHINKDB_PORT', '28015'))
    database = os.environ.get('RETHINKDB_DATABASE', '<database>')
    username = os.environ.get('RETHINKDB_USERNAME', '<username>')
    password = os.environ.get('RETHINKDB_PASSWORD', '<password>')
    conn = r.connect(
        host=host,
        port=port,
        db=database,
        user=username,
        password=password
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        r = RethinkDB()
        result = r.db("rethinkdb").table("server_status").run(conn)
        print(f"RethinkDB connected. Server: {list(result)[0]['name']}")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to RethinkDB: {e}")
