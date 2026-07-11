"""Supabase connector using supabase-py."""

import os

from supabase import create_client, Client


def connect() -> Client:
    """Connect to Supabase.

    Environment variables:
        SUPABASE_URL: Supabase project URL (e.g., https://<project-id>.supabase.co)
        SUPABASE_KEY: Supabase anon/service key
    """
    url = os.environ.get('SUPABASE_URL', 'https://<project-id>.supabase.co')
    key = os.environ.get('SUPABASE_KEY', '<anon-key>')
    client = create_client(url, key)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        response = client.table("<table>").select("*").limit(1).execute()
        print(f"Supabase connected. Response: {response}")
    except Exception as e:
        print(f"Error connecting to Supabase: {e}")
