import asyncio
from network import GameClient


async def main():
    client = GameClient()
    await client.connect()
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
