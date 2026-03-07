from firebolt.db import connect as firebolt_connect

def connect():
    conn = firebolt_connect(
        engine_name="<engine>",
        database="<database>",
        username="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"Firebolt version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
