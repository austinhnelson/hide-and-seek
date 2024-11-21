import pygame
from config import DISPLAY
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
        while self.game_state.running:
            self.game_state.run(self.window)

            self.clock.tick(DISPLAY["FPS"])

        await self.game_state.shutdown()
