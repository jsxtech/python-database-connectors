import teradatasql

def connect():
    conn = teradatasql.connect(
        host="<host>",
        user="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT InfoData FROM DBC.DBCInfoV WHERE InfoKey = 'VERSION'")
    print(f"Teradata version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
