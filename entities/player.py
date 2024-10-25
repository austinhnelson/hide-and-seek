import pygame
import math
from config import MAP, PLAYER, TILE


class Player:
    def __init__(self):
        self.position_x = PLAYER["INITIAL_X"]
        self.position_y = PLAYER["INITIAL_Y"]
        self.radius = PLAYER["RADIUS"]
        self.player_angle = math.pi

    def __move(self, direction_multiplier):
        new_x = self.position_x + \
            (-math.sin(self.player_angle) * 5 * direction_multiplier)
        new_y = self.position_y + \
            (math.cos(self.player_angle) * 5 * direction_multiplier)

        col = int(new_x / TILE["WIDTH"])
        row = int(new_y / TILE["HEIGHT"])
        square = row * MAP["WIDTH"] + col

        if MAP["BOARD"][square] != '#':
            self.position_x = new_x
            self.position_y = new_y

    def move_forward(self):
        self.__move(1)

    def move_backward(self):
        self.__move(-1)

    def look_left(self):
        self.player_angle -= 0.1

    def look_right(self):
        self.player_angle += 0.1

    def draw(self, window):
        pygame.draw.circle(window, PLAYER["COLOR"], (
            self.position_x, self.position_y), self.radius)
