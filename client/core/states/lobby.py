from .base import StateBase
from ui import Lobby
import pygame


class LobbyState(StateBase):
    def __init__(self, game_state):
        self.menu = Lobby()
        self.game_state = game_state
        self.client = self.game_state.client

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                from .menu import MenuState
                self.game_state.set_state(MenuState(self.game_state))
            if event.key == pygame.K_SPACE:
                self.client.toggle_ready()

    def render(self, window):
        self.menu.draw(
            window, self.client.player_data["players"], self.client.client_id)

    def run(self):
        # Determines when the game can actually be started.
        is_all_ready = all(player["ready"]
                           for player in self.client.player_data["players"])
        if is_all_ready and self.client.player_data["player_count"] > 1:
            from .playing import PlayingState
            self.game_state.set_state(PlayingState(self.game_state))
