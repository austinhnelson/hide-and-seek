from .base import StateBase
from ui import Lobby
import pygame
from network import GameClient


class LobbyState(StateBase):
    def __init__(self, game_state):
        self.menu = Lobby()
        self.client = GameClient()
        self.game_state = game_state
        self.ready = False

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                from .menu import MenuState
                self.game_state.set_state(MenuState(self.game_state))

    def render(self, window):
        self.menu.draw(window, [])
