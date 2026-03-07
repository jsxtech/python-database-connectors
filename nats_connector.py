import nats

def connect():
    return "nats://localhost:4222"

async def connect_async():
    nc = await nats.connect("nats://localhost:4222")
    return nc

if __name__ == "__main__":
    import asyncio
    
    async def main():
        nc = await connect_async()
        print(f"NATS connected. Client ID: {nc.client_id}")
        await nc.close()
    
    asyncio.run(main())
