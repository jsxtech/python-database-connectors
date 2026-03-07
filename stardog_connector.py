from stardog import Connection

def connect():
    conn = Connection(
        "stardog",
        endpoint="http://localhost:5820",
        username="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    result = conn.select("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
    print(f"Stardog connected. Result: {result}")
    conn.close()
