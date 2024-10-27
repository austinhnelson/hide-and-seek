from network import GameServer
import asyncio


async def main():
    server = GameServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
