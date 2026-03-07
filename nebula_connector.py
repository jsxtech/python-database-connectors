from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config

def connect():
    config = Config()
    connection_pool = ConnectionPool()
    connection_pool.init([("localhost", 9669)], config)
    return connection_pool

if __name__ == "__main__":
    pool = connect()
    session = pool.get_session("<username>", "<password>")
    result = session.execute("SHOW HOSTS")
    print(f"NebulaGraph connected. Result: {result}")
    session.release()
    pool.close()
