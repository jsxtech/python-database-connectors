from rethinkdb import RethinkDB

def connect():
    r = RethinkDB()
    conn = r.connect(
        host="localhost",
        port=28015,
        db="<database>",
        user="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    r = RethinkDB()
    result = r.db("rethinkdb").table("server_status").run(conn)
    print(f"RethinkDB connected. Server: {list(result)[0]['name']}")
    conn.close()
