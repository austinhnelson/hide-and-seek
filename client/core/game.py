import sys
import pygame
import asyncio
from config import DISPLAY
from network import GameClient


class GameState:
    MENU = "menu",
    PLAYING = "playing"


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode(
            (DISPLAY["WIDTH"], DISPLAY["HEIGHT"]))
        pygame.display.set_caption(DISPLAY["CAPTION"])
        self.clock = pygame.time.Clock()

        self.client = GameClient()

        self.running = True
        self.state = GameState.MENU

    async def run(self):
        connect_task = asyncio.create_task(self.client.connect())

        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(DISPLAY["FPS"])
            await asyncio.sleep(0)

        await connect_task
        await self.shutdown()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.state == GameState.MENU:
                    self.state = GameState.PLAYING

    def render(self):
        self.window.fill((0, 0, 0))

        if self.state == GameState.MENU:
            self.window.fill((0, 0, 0))
        elif self.state == GameState.PLAYING:
            self.window.fill((255, 255, 255))

        pygame.display.flip()

    async def shutdown(self):
        await self.client.disconnect()
        pygame.quit()
        sys.exit(0)
