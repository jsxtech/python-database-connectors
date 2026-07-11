"""IBM DB2 database connector."""

import os

import ibm_db


def connect() -> ibm_db.IBM_DBConnection:
    """Connect to an IBM DB2 database.

    Environment variables:
        DB2_HOST: Database host (default: localhost)
        DB2_PORT: Database port (default: 50000)
        DB2_DATABASE: Database name
        DB2_USER: Database username
        DB2_PASSWORD: Database password

    Returns:
        An IBM DB2 connection object.
    """
    host = os.environ.get("DB2_HOST", "localhost")
    port = os.environ.get("DB2_PORT", "50000")
    database = os.environ.get("DB2_DATABASE", "<database>")
    user = os.environ.get("DB2_USER", "<username>")
    password = os.environ.get("DB2_PASSWORD", "<password>")
    conn_str = f"DATABASE={database};HOSTNAME={host};PORT={port};PROTOCOL=TCPIP;UID={user};PWD={password};"
    conn = ibm_db.connect(conn_str, "", "")
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        server_info = ibm_db.server_info(conn)
        print(f"IBM DB2 version: {server_info.DBMS_VER}")
        ibm_db.close(conn)
    except Exception as e:
        print(f"Failed to connect to IBM DB2: {e}")
