"""Databricks SQL connector using databricks-sql-connector."""

import os

from databricks import sql
from databricks.sql.client import Connection


def connect() -> Connection:
    """Connect to Databricks SQL.

    Environment variables:
        DATABRICKS_SERVER_HOSTNAME: Workspace URL
        DATABRICKS_HTTP_PATH: SQL warehouse HTTP path
        DATABRICKS_ACCESS_TOKEN: Personal access token
    """
    conn = sql.connect(
        server_hostname=os.environ.get('DATABRICKS_SERVER_HOSTNAME', '<workspace-url>'),
        http_path=os.environ.get('DATABRICKS_HTTP_PATH', '<http-path>'),
        access_token=os.environ.get('DATABRICKS_ACCESS_TOKEN', '<access-token>')
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT current_version()")
        print(f"Databricks version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to Databricks: {e}")
