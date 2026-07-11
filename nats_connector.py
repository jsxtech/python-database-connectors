"""NATS connector using the nats-py async client."""

import asyncio
import os

import nats


def connect() -> nats.NATS:
    """Connect to NATS and return the client.

    Wraps the async connection in asyncio.run() for a synchronous interface.

    Environment Variables:
        NATS_URL: NATS server URL (default: nats://localhost:4222)

    Returns:
        A connected NATS client.
    """
    url = os.environ.get("NATS_URL", "nats://localhost:4222")
    loop = asyncio.new_event_loop()
    nc = loop.run_until_complete(nats.connect(url))
    return nc


if __name__ == "__main__":
    try:
        nc = connect()
        print(f"NATS connected. Client ID: {nc.client_id}")
        asyncio.run(nc.close())
    except Exception as e:
        print(f"Failed to connect to NATS: {e}")
