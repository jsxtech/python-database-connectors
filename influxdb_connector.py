"""InfluxDB connector using the influxdb-client-python library."""

import os

from influxdb_client import InfluxDBClient


def connect() -> InfluxDBClient:
    """Connect to InfluxDB and return the client.

    Environment Variables:
        INFLUXDB_URL: InfluxDB server URL (default: http://localhost:8086)
        INFLUXDB_TOKEN: Authentication token
        INFLUXDB_ORG: Organization name
    """
    url = os.environ.get('INFLUXDB_URL', 'http://localhost:8086')
    token = os.environ.get('INFLUXDB_TOKEN', '<token>')
    org = os.environ.get('INFLUXDB_ORG', '<org>')

    client = InfluxDBClient(
        url=url,
        token=token,
        org=org
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        health = client.health()
        print(f"InfluxDB status: {health.status}, version: {health.version}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to InfluxDB: {e}")
