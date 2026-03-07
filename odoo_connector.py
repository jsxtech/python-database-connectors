import xmlrpc.client

def connect():
    url = "http://localhost:8069"
    db = "<database>"
    username = "<username>"
    password = "<password>"
    
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
