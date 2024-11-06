from .base import StateBase
from ui import Lobby
import pygame


class LobbyState(StateBase):
    def __init__(self, game_state):
        self.menu = Lobby()
        self.game_state = game_state
        self.ready = False

    def handle_input(self, event):
        pass

    def render(self, window):
        self.menu.draw(window)
