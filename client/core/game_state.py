import sys
import pygame

from .states import MenuState
from network import GameClient
from .states import LobbyState


class GameState:
    def __init__(self):
        self.client = None
        self.state = MenuState(self)
        self.running = True

    def run(self, window):
        self.__handle_events()
        self.__render(window)

    async def shutdown(self):
        if self.client:
            self.client.close()
        pygame.quit()
        sys.exit(0)

    def set_state(self, new_state):
        if isinstance(self.state, LobbyState) and self.client:
            self.client.close()
            self.client = None

        self.state = new_state

    def initializeClient(self):
        if not self.client:
            self.client = GameClient()

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
