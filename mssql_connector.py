"""MS SQL Server database connector."""

import os

import pyodbc


def connect() -> pyodbc.Connection:
    """Connect to a MS SQL Server database.

    Environment variables:
        MSSQL_DRIVER: ODBC driver (default: ODBC Driver 18 for SQL Server)
        MSSQL_SERVER: Database server
        MSSQL_DATABASE: Database name
        MSSQL_USER: Database username
        MSSQL_PASSWORD: Database password

    Returns:
        A MS SQL Server connection object.
    """
    driver = os.environ.get("MSSQL_DRIVER", "ODBC Driver 18 for SQL Server")
    server = os.environ.get("MSSQL_SERVER", "<server>")
    database = os.environ.get("MSSQL_DATABASE", "<database>")
    user = os.environ.get("MSSQL_USER", "<username>")
    password = os.environ.get("MSSQL_PASSWORD", "<password>")
    conn = pyodbc.connect(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password}"
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        print(f"MS SQL Server version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to MS SQL Server: {e}")
