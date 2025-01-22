from .base import StateBase
from ui import Map


class PlayingState(StateBase):
    def __init__(self, game_state):
        self.map = Map()
        self.game_state = game_state
        self.client = self.game_state.client

    def handle_input(self, event):
        pass

    def render(self, window):
        self.map.draw(window)
