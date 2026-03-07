import boto3

def connect():
    client = boto3.client(
        "timestream-write",
        region_name="<region>",
        aws_access_key_id="<access-key>",
        aws_secret_access_key="<secret-key>"
    )
    return client

if __name__ == "__main__":
    client = connect()
    databases = client.list_databases()
    print(f"Timestream connected. Databases: {[db['DatabaseName'] for db in databases['Databases']]}")
