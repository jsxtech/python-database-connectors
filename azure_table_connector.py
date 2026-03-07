from azure.data.tables import TableServiceClient

def connect():
    connection_string = "<connection-string>"
    service = TableServiceClient.from_connection_string(conn_str=connection_string)
    return service

if __name__ == "__main__":
    service = connect()
    tables = service.list_tables()
    print(f"Azure Table Storage connected. Tables: {[t.name for t in tables]}")
