import sys
import pygame
from .states import MenuState
from network import GameClient


class GameState:
    def __init__(self):
        self.state = MenuState(self)
        self.client = GameClient()
        self.running = True

    def run(self, window):
        self.player_list = self.client.player_list
        self.__handle_events()
        self.__render(window)

    async def shutdown(self):
        await self.client.disconnect()

        pygame.quit()
        sys.exit(0)

    def set_state(self, new_state):
        self.state = new_state

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.state.handle_input(event)

    def __render(self, window):
        window.fill((0, 0, 0))

        self.state.render(window)

        pygame.display.flip()
