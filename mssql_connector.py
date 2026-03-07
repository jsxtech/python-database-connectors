import pyodbc

def connect():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=<server>;"
        "DATABASE=<database>;"
        "UID=<username>;"
        "PWD=<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    print(f"MS SQL Server version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
