from pydruid.db import connect as druid_connect

def connect():
    conn = druid_connect(
        host="localhost",
        port=8082,
        path="/druid/v2/sql/",
        scheme="http"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print(f"Druid connected. Test query: {cursor.fetchone()}")
    cursor.close()
    conn.close()
