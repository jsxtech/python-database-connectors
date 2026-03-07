from influxdb_client import InfluxDBClient

def connect():
    client = InfluxDBClient(
        url="http://localhost:8086",
        token="<token>",
        org="<org>"
    )
    return client

if __name__ == "__main__":
    client = connect()
    health = client.health()
    print(f"InfluxDB status: {health.status}, version: {health.version}")
    client.close()
