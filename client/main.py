import asyncio
from core import Game


async def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    asyncio.run(main())
