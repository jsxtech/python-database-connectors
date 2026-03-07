import requests

def connect():
    return {
        "url": "https://<database>.turso.io",
        "token": "<auth-token>"
    }

def query(config, sql):
    headers = {"Authorization": f"Bearer {config['token']}"}
    response = requests.post(config["url"], headers=headers, json={"statements": [sql]})
    return response.json()

if __name__ == "__main__":
    config = connect()
    result = query(config, "SELECT 1")
    print(f"Turso connected. Result: {result}")
