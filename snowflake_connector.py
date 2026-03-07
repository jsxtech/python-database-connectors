import snowflake.connector

def connect():
    conn = snowflake.connector.connect(
        user="<username>",
        password="<password>",
        account="<account>",
        warehouse="<warehouse>",
        database="<database>",
        schema="<schema>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_VERSION()")
    print(f"Snowflake version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
