from .base import StateBase


class LobbyState(StateBase):
    def __init__(self, menu):
        self.menu = menu

    def handle_input(self, event):
        pass

    def render(self, window):
        self.menu.draw_lobby(window)
