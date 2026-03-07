from pyhive import hive

def connect():
    conn = hive.Connection(
        host="localhost",
        port=10000,
        username="<username>",
        database="<database>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"Hive version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
