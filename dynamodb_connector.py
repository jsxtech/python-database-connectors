import boto3

def connect():
    dynamodb = boto3.resource(
        "dynamodb",
        region_name="<region>",
        aws_access_key_id="<access-key>",
        aws_secret_access_key="<secret-key>"
    )
    return dynamodb

if __name__ == "__main__":
    dynamodb = connect()
    tables = list(dynamodb.tables.all())
    print(f"DynamoDB connected. Tables: {[t.name for t in tables]}")
