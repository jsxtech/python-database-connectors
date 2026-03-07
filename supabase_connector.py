from supabase import create_client

def connect():
    url = "https://<project-id>.supabase.co"
    key = "<anon-key>"
    client = create_client(url, key)
    return client

if __name__ == "__main__":
    client = connect()
    response = client.table("<table>").select("*").limit(1).execute()
    print(f"Supabase connected. Response: {response}")
