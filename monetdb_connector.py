import pymonetdb

def connect():
    conn = pymonetdb.connect(
        hostname="localhost",
        port=50000,
        username="<username>",
        password="<password>",
        database="<database>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"MonetDB version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
