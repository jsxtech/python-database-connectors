import requests

def connect():
    return "http://localhost:4001"

def query(url, sql):
    response = requests.post(f"{url}/db/query", json=[[sql]])
    return response.json()

if __name__ == "__main__":
    url = connect()
    result = query(url, "SELECT 1")
    print(f"rqlite connected. Result: {result}")
