import sys
import pygame

from .states import MenuState
from network import GameClient
from .states import LobbyState
from .states import PlayingState


class GameState:
    def __init__(self):
        self.client = None
        self.state = MenuState(self)
        self.running = True

    def run(self, window):
        self.__handle_events()
        self.__render(window)
        self.__run()

    async def shutdown(self):
        if self.client:
            self.client.close()
        pygame.quit()
        sys.exit(0)

    def set_state(self, new_state):
        if isinstance(self.state, LobbyState) and not isinstance(new_state, PlayingState):
            self.client.close()
            self.client = None

        self.state = new_state

    def initializeClient(self):
        if not self.client:
            try:
                self.client = GameClient()
                return True
            except Exception as ex:
                print(f"Error connecting to server, is it running? ")
                return False

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

    def __run(self):
        self.state.run()
