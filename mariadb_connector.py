import mariadb

def connect():
    conn = mariadb.connect(
        host="localhost",
        user="<username>",
        password="<password>",
        database="<database>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    print(f"MariaDB version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
