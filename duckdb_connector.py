import duckdb

def connect():
    conn = duckdb.connect(database="<database>.db")
    return conn

if __name__ == "__main__":
    conn = connect()
    result = conn.execute("SELECT version()").fetchone()
    print(f"DuckDB version: {result[0]}")
    conn.close()
