from google.cloud import spanner

def connect():
    client = spanner.Client(project="<project-id>")
    instance = client.instance("<instance-id>")
    database = instance.database("<database-id>")
    return database

if __name__ == "__main__":
    database = connect()
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql("SELECT 1")
        print(f"Cloud Spanner connected. Test query: {list(results)}")
