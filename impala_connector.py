from impala.dbapi import connect as impala_connect

def connect():
    conn = impala_connect(
        host="localhost",
        port=21050,
        database="<database>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"Impala version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
