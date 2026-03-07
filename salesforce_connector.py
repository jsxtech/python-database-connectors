import pyodbc

def connect():
    conn = pyodbc.connect(
        "DRIVER={Salesforce ODBC Driver};"
        "UID=<username>;"
        "PWD=<password>;"
        "SecurityToken=<token>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Name FROM Account LIMIT 1")
    print(f"Salesforce connected. Result: {cursor.fetchone()}")
    cursor.close()
    conn.close()
