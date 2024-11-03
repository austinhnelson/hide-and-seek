from .base import StateBase


class MenuState(StateBase):
    def __init__(self, menu):
        self.menu = menu

    def handle_input(self, event):
        pass

    def render(self, window):
        self.menu.draw_menu(window)
