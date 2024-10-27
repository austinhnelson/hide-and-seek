import asyncio
from network import GameServer


async def main():
    server = GameServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
