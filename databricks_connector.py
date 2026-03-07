from databricks import sql

def connect():
    conn = sql.connect(
        server_hostname="<workspace-url>",
        http_path="<http-path>",
        access_token="<access-token>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT current_version()")
    print(f"Databricks version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
