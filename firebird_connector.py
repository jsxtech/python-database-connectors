import fdb

def connect():
    conn = fdb.connect(
        host="localhost",
        database="<database-path>",
        user="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT rdb$get_context('SYSTEM', 'ENGINE_VERSION') FROM rdb$database")
    print(f"Firebird version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
