"""Rockset connector using the rockset-python-client library."""

import os

from rockset import RocksetClient


def connect() -> RocksetClient:
    """Connect to Rockset and return the client.

    Environment Variables:
        ROCKSET_API_KEY: Rockset API key
        ROCKSET_API_SERVER: Rockset API server (e.g., us-west-2.rockset.com)
    """
    api_key = os.environ.get('ROCKSET_API_KEY', '<api-key>')
    api_server = os.environ.get('ROCKSET_API_SERVER', '<region>.rockset.com')

    client = RocksetClient(api_key=api_key, api_server=api_server)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        workspaces = client.Workspaces.list()
        print(f"Rockset connected. Workspaces: {[w.name for w in workspaces.data]}")
    except Exception as e:
        print(f"Failed to connect to Rockset: {e}")
