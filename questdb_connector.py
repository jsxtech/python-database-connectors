import questdb

def connect():
    from questdb.ingress import Sender
    with Sender("localhost", 9009) as sender:
        return sender

if __name__ == "__main__":
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        port=8812,
        user="admin",
        password="quest",
        database="qdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print(f"QuestDB connected. Test query: {cursor.fetchone()}")
    cursor.close()
    conn.close()
