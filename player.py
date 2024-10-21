import pygame
import math
from constants import PlayerConstants
from constants import MapConstants


class Player:
    def __init__(self, position_x, position_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.player_angle = math.pi

    def move(self, direction_multiplier):
        new_x = self.position_x + \
            (-math.sin(self.player_angle) * 5 * direction_multiplier)
        new_y = self.position_y + \
            (math.cos(self.player_angle) * 5 * direction_multiplier)

        col = int(new_x / MapConstants.TILE_WIDTH)
        row = int(new_y / MapConstants.TILE_HEIGHT)
        square = row * MapConstants.MAP_WIDTH + col

        if MapConstants.MAP[square] != '#':
            self.position_x = new_x
            self.position_y = new_y

    def move_forward(self):
        self.move(1)

    def move_backward(self):
        self.move(-1)

    def move_left(self):
        self.player_angle -= 0.1

    def move_right(self):
        self.player_angle += 0.1

    def draw(self, window):
        pygame.draw.circle(window, PlayerConstants.PLAYER_COLOR, (
            self.position_x, self.position_y), self.radius)
