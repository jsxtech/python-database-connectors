import sqlite3

def connect():
    conn = sqlite3.connect("<database>.db")
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version()")
    print(f"SQLite version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
