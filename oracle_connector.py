import oracledb

def connect():
    conn = oracledb.connect(
        user="<username>",
        password="<password>",
        dsn="<host>:<port>/<service_name>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT banner FROM v$version WHERE banner LIKE 'Oracle%'")
    print(f"Oracle version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
