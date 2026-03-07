from exasol.websocket import connect as exasol_connect

def connect():
    conn = exasol_connect(
        dsn="<host>:8563",
        user="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.execute("SELECT PARAM_VALUE FROM EXA_METADATA WHERE PARAM_NAME='databaseProductVersion'")
    print(f"Exasol version: {cursor.fetchone()[0]}")
    conn.close()
