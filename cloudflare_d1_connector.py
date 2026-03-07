import requests

def connect():
    account_id = "<account-id>"
    database_id = "<database-id>"
    api_token = "<api-token>"
    
    return {
        "account_id": account_id,
        "database_id": database_id,
        "api_token": api_token,
        "base_url": f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database/{database_id}"
    }

def query(config, sql):
    headers = {"Authorization": f"Bearer {config['api_token']}"}
    response = requests.post(f"{config['base_url']}/query", headers=headers, json={"sql": sql})
    return response.json()

if __name__ == "__main__":
    config = connect()
    result = query(config, "SELECT 1 as test")
    print(f"Cloudflare D1 connected. Result: {result}")
