"""Azure Table Storage connector using azure-data-tables."""

import os

from azure.data.tables import TableServiceClient


def connect() -> TableServiceClient:
    """Connect to Azure Table Storage.

    Environment variables:
        AZURE_TABLE_CONNECTION_STRING: Azure Storage connection string
    """
    connection_string = os.environ.get('AZURE_TABLE_CONNECTION_STRING', '<connection-string>')
    service = TableServiceClient.from_connection_string(conn_str=connection_string)
    return service


if __name__ == "__main__":
    try:
        service = connect()
        tables = service.list_tables()
        print(f"Azure Table Storage connected. Tables: {[t.name for t in tables]}")
    except Exception as e:
        print(f"Error connecting to Azure Table Storage: {e}")
