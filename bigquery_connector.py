from google.cloud import bigquery

def connect():
    client = bigquery.Client(project="<project-id>")
    return client

if __name__ == "__main__":
    client = connect()
    query = "SELECT 1 as test"
    result = client.query(query).result()
    print(f"BigQuery connected. Test query result: {list(result)}")
