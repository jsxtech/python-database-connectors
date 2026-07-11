"""HBase connector using the happybase library."""

import os

import happybase


def connect() -> happybase.Connection:
    """Connect to HBase and return the connection.

    Environment Variables:
        HBASE_HOST: HBase Thrift server host (default: localhost)
        HBASE_PORT: HBase Thrift server port (default: 9090)
    """
    host = os.environ.get('HBASE_HOST', 'localhost')
    port = int(os.environ.get('HBASE_PORT', '9090'))

    conn = happybase.Connection(host=host, port=port)
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        tables = conn.tables()
        print(f"HBase connected. Tables: {tables}")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to HBase: {e}")
