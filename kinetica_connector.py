import kinetica

def connect():
    options = kinetica.GPUdbConnectionOptions()
    options.host = "localhost"
    options.port = "9191"
    options.username = "<username>"
    options.password = "<password>"
    
    db = kinetica.GPUdb(host=options.host, options=options)
    return db

if __name__ == "__main__":
    db = connect()
    response = db.show_system_properties()
    print(f"Kinetica connected. Version: {response['property_map']['version.gpudb_core_version']}")
