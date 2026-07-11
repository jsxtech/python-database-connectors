"""SurrealDB connector using surrealdb-py."""

import asyncio
import os

from surrealdb import Surreal


def connect() -> Surreal:
    """Connect to SurrealDB and return the client.

    Uses asyncio internally since the SurrealDB Python client is async.

    Environment variables:
        SURREALDB_URL: SurrealDB WebSocket URL (default: ws://localhost:8000/rpc)
        SURREALDB_USERNAME: Authentication username
        SURREALDB_PASSWORD: Authentication password
        SURREALDB_NAMESPACE: Namespace to use
        SURREALDB_DATABASE: Database to use

    Returns:
        A connected SurrealDB client.
    """
    url = os.environ.get("SURREALDB_URL", "ws://localhost:8000/rpc")
    username = os.environ.get("SURREALDB_USERNAME", "<username>")
    password = os.environ.get("SURREALDB_PASSWORD", "<password>")
    namespace = os.environ.get("SURREALDB_NAMESPACE", "<namespace>")
    database = os.environ.get("SURREALDB_DATABASE", "<database>")

    async def _connect():
        db = Surreal(url)
        await db.connect()
        await db.signin({"user": username, "pass": password})
        await db.use(namespace, database)
        return db

    loop = asyncio.new_event_loop()
    db = loop.run_until_complete(_connect())
    return db


if __name__ == "__main__":
    try:
        db = connect()

        async def _query():
            result = await db.query("INFO FOR DB")
            print(f"SurrealDB connected. Info: {result}")
            await db.close()

        asyncio.run(_query())
    except Exception as e:
        print(f"Failed to connect to SurrealDB: {e}")
