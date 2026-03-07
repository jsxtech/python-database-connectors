import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host="<host>.psdb.cloud",
        user="<username>",
        password="<password>",
        database="<database>",
        ssl_ca="/etc/ssl/cert.pem"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    print(f"PlanetScale version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
