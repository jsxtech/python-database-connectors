"""Salesforce connector using simple-salesforce."""

import os

from simple_salesforce import Salesforce


def connect() -> Salesforce:
    """Connect to Salesforce and return the client.

    Environment variables:
        SALESFORCE_USERNAME: Salesforce username
        SALESFORCE_PASSWORD: Salesforce password
        SALESFORCE_TOKEN: Salesforce security token
        SALESFORCE_DOMAIN: Login domain (default: login, use 'test' for sandbox)

    Returns:
        A Salesforce client instance.
    """
    username = os.environ.get("SALESFORCE_USERNAME", "<username>")
    password = os.environ.get("SALESFORCE_PASSWORD", "<password>")
    token = os.environ.get("SALESFORCE_TOKEN", "<security-token>")
    domain = os.environ.get("SALESFORCE_DOMAIN", "login")

    sf = Salesforce(
        username=username,
        password=password,
        security_token=token,
        domain=domain,
    )
    return sf


if __name__ == "__main__":
    try:
        sf = connect()
        result = sf.query("SELECT Id, Name FROM Account LIMIT 1")
        print(f"Salesforce connected. Records: {result['totalSize']}")
    except Exception as e:
        print(f"Failed to connect to Salesforce: {e}")
