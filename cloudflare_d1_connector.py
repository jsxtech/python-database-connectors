"""Cloudflare D1 connector using requests."""

import os

import requests


def connect() -> dict:
    """Connect to Cloudflare D1 and return configuration dict.

    Environment variables:
        CLOUDFLARE_D1_ACCOUNT_ID: Cloudflare account ID
        CLOUDFLARE_D1_DATABASE_ID: D1 database ID
        CLOUDFLARE_D1_API_TOKEN: Cloudflare API token
    """
    account_id = os.environ.get('CLOUDFLARE_D1_ACCOUNT_ID', '<account-id>')
    database_id = os.environ.get('CLOUDFLARE_D1_DATABASE_ID', '<database-id>')
    api_token = os.environ.get('CLOUDFLARE_D1_API_TOKEN', '<api-token>')

    return {
        "account_id": account_id,
        "database_id": database_id,
        "api_token": api_token,
        "base_url": f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database/{database_id}"
    }


def query(config: dict, sql: str) -> dict:
    """Execute a SQL query against Cloudflare D1."""
    headers = {"Authorization": f"Bearer {config['api_token']}"}
    response = requests.post(f"{config['base_url']}/query", headers=headers, json={"sql": sql})
    return response.json()


if __name__ == "__main__":
    try:
        config = connect()
        result = query(config, "SELECT 1 as test")
        print(f"Cloudflare D1 connected. Result: {result}")
    except Exception as e:
        print(f"Error connecting to Cloudflare D1: {e}")
