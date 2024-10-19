import pygame
from constants import PlayerConstants


class Player:
    def __init__(self, position_x, position_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

    def draw(self, window):
        pygame.draw.circle(window, PlayerConstants.PLAYER_COLOR, (
            self.position_x, self.position_y), self.radius)
