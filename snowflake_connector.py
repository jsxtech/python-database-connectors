"""Snowflake connector using snowflake-connector-python."""

import os

import snowflake.connector
from snowflake.connector.connection import SnowflakeConnection


def connect() -> SnowflakeConnection:
    """Connect to Snowflake.

    Environment variables:
        SNOWFLAKE_USER: Username
        SNOWFLAKE_PASSWORD: Password
        SNOWFLAKE_ACCOUNT: Account identifier
        SNOWFLAKE_WAREHOUSE: Warehouse name
        SNOWFLAKE_DATABASE: Database name
        SNOWFLAKE_SCHEMA: Schema name
    """
    conn = snowflake.connector.connect(
        user=os.environ.get('SNOWFLAKE_USER', '<username>'),
        password=os.environ.get('SNOWFLAKE_PASSWORD', '<password>'),
        account=os.environ.get('SNOWFLAKE_ACCOUNT', '<account>'),
        warehouse=os.environ.get('SNOWFLAKE_WAREHOUSE', '<warehouse>'),
        database=os.environ.get('SNOWFLAKE_DATABASE', '<database>'),
        schema=os.environ.get('SNOWFLAKE_SCHEMA', '<schema>')
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION()")
        print(f"Snowflake version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
