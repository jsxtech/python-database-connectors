"""Odoo ERP connector using XML-RPC."""

import os
import xmlrpc.client
from typing import Dict, Any


def connect() -> Dict[str, Any]:
    """Connect to Odoo via XML-RPC and return a connection dict.

    Returns a dictionary with url, db, uid, password, and models proxy.

    Environment Variables:
        ODOO_URL: Odoo server URL (default: http://localhost:8069)
        ODOO_DATABASE: Odoo database name
        ODOO_USERNAME: Odoo username
        ODOO_PASSWORD: Odoo password
    """
    url = os.environ.get('ODOO_URL', 'http://localhost:8069')
    db = os.environ.get('ODOO_DATABASE', '<database>')
    username = os.environ.get('ODOO_USERNAME', '<username>')
    password = os.environ.get('ODOO_PASSWORD', '<password>')

    common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
    uid = common.authenticate(db, username, password, {})

    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

    return {
        "url": url,
        "db": db,
        "uid": uid,
        "password": password,
        "models": models
    }


if __name__ == "__main__":
    try:
        conn = connect()

        # Test connection by getting server version
        common = xmlrpc.client.ServerProxy(f"{conn['url']}/xmlrpc/2/common")
        version = common.version()
        print(f"Odoo version: {version['server_version']}")

        # Example: Read partner records
        partners = conn["models"].execute_kw(
            conn["db"], conn["uid"], conn["password"],
            "res.partner", "search_read",
            [[]], {"fields": ["name"], "limit": 1}
        )
        print(f"Sample partner: {partners}")
    except Exception as e:
        print(f"Failed to connect to Odoo: {e}")
