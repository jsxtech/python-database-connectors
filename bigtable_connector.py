from google.cloud import bigtable

def connect():
    client = bigtable.Client(project="<project-id>", admin=True)
    instance = client.instance("<instance-id>")
    return instance

if __name__ == "__main__":
    instance = connect()
    tables = instance.list_tables()
    print(f"Bigtable connected. Tables: {[t.table_id for t in tables]}")
