"""ClickHouse connector using the clickhouse-connect library."""

import os

import clickhouse_connect
from clickhouse_connect.driver import Client


def connect() -> Client:
    """Connect to ClickHouse and return the client.

    Environment Variables:
        CLICKHOUSE_HOST: ClickHouse server host (default: localhost)
        CLICKHOUSE_PORT: ClickHouse HTTP port (default: 8123)
        CLICKHOUSE_USERNAME: Authentication username
        CLICKHOUSE_PASSWORD: Authentication password
    """
    host = os.environ.get('CLICKHOUSE_HOST', 'localhost')
    port = int(os.environ.get('CLICKHOUSE_PORT', '8123'))
    username = os.environ.get('CLICKHOUSE_USERNAME', '<username>')
    password = os.environ.get('CLICKHOUSE_PASSWORD', '<password>')

    client = clickhouse_connect.get_client(
        host=host,
        port=port,
        username=username,
        password=password
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        result = client.query("SELECT version()")
        print(f"ClickHouse version: {result.result_rows[0][0]}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to ClickHouse: {e}")
