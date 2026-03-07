import ibm_db

def connect():
    conn_str = "DATABASE=<database>;HOSTNAME=<host>;PORT=50000;PROTOCOL=TCPIP;UID=<username>;PWD=<password>;"
    conn = ibm_db.connect(conn_str, "", "")
    return conn

if __name__ == "__main__":
    conn = connect()
    server_info = ibm_db.server_info(conn)
    print(f"IBM DB2 version: {server_info.DBMS_VER}")
    ibm_db.close(conn)
