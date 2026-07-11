"""Apache Druid connector using the pydruid library."""

import os

from pydruid.db import connect as druid_connect
from pydruid.db.api import Connection


def connect() -> Connection:
    """Connect to Apache Druid and return the DB-API connection.

    Environment Variables:
        DRUID_HOST: Druid broker host (default: localhost)
        DRUID_PORT: Druid broker port (default: 8082)
        DRUID_PATH: SQL endpoint path (default: /druid/v2/sql/)
        DRUID_SCHEME: Connection scheme (default: http)
    """
    host = os.environ.get('DRUID_HOST', 'localhost')
    port = int(os.environ.get('DRUID_PORT', '8082'))
    path = os.environ.get('DRUID_PATH', '/druid/v2/sql/')
    scheme = os.environ.get('DRUID_SCHEME', 'http')

    conn = druid_connect(
        host=host,
        port=port,
        path=path,
        scheme=scheme
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        print(f"Druid connected. Test query: {cursor.fetchone()}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Druid: {e}")
