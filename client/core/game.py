import sys
import pygame
import asyncio
from config import DISPLAY
from network import GameClient
from ui import Menu
from .game_state import GameState


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode(
            (DISPLAY["WIDTH"], DISPLAY["HEIGHT"]))
        pygame.display.set_caption(DISPLAY["CAPTION"])
        self.clock = pygame.time.Clock()

        self.game_state = GameState()

    async def run(self):
        # connect_task = asyncio.create_task(self.client.connect())

        while self.game_state.running:
            self.handle_events()
            # await self.client.process_server_messages()
            self.render()
            self.clock.tick(DISPLAY["FPS"])
            await asyncio.sleep(0)

        # await connect_task
        await self.shutdown()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.running = False
            else:
                self.game_state.handle_input(event)

    def render(self):
        self.window.fill((0, 0, 0))
        self.game_state.render(self.window)
        pygame.display.flip()

    async def shutdown(self):
        # await self.client.disconnect()
        pygame.quit()
        sys.exit(0)
