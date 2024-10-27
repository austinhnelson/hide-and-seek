import pygame
import asyncio
import sys
from config import DISPLAY
from network import GameClient


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode(
            (DISPLAY["WIDTH"], DISPLAY["HEIGHT"]))
        pygame.display.set_caption(DISPLAY["CAPTION"])
        self.clock = pygame.time.Clock()

        self.client = GameClient()

        self.running = True

        self.loop = asyncio.new_event_loop()
        self.connect_players = self.loop.create_task(self.client.connect())

    def run(self):
        try:
            while self.running:
                self.render()
                self.clock.tick(DISPLAY["FPS"])

                # TODO: Is this the best approach?
                self.loop.call_soon(self.loop.stop)
                self.loop.run_forever()
        finally:
            self.shutdown()

    def render(self):
        self.window.fill((0, 0, 0))
        pygame.display.flip()

    def shutdown(self):
        self.connect_players.cancel()
        try:
            self.loop.run_until_complete(self.connect_players)
        except asyncio.CancelledError:
            print("Program closing...")

        self.loop.close()
        pygame.quit()
        sys.exit(0)
