from tigergraph import TigerGraphConnection

def connect():
    conn = TigerGraphConnection(
        host="http://localhost",
        graphname="<graph>",
        username="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    version = conn.getVersion()
    print(f"TigerGraph version: {version}")
