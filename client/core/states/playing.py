import pygame
from .base import StateBase
from ui import Map


class PlayingState(StateBase):
    def __init__(self, game_state):
        self.map = Map()
        self.game_state = game_state
        self.client = self.game_state.client
        self.player_x = 200
        self.player_y = 200

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.player_x -= 10
            elif event.key == pygame.K_d:
                self.player_x += 10
            elif event.key == pygame.K_w:
                self.player_y -= 10
            elif event.key == pygame.K_s:
                self.player_y += 10

    def render(self, window):
        self.map.draw(
            window, self.client.player_data["players"], self.player_x, self.player_y)

    def run(self):
        self.client.update_position(self.player_x, self.player_y)
