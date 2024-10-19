import pygame
import math
from constants import PlayerConstants


class Player:
    def __init__(self, position_x, position_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.player_angle = math.pi

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] | keys[pygame.K_a]:
            self.player_angle -= 0.1
        if keys[pygame.K_RIGHT] | keys[pygame.K_d]:
            self.player_angle += 0.1

    def ray_casting(self):
        pass

    def draw(self, window):
        FOV = math.pi / 3
        HALF_FOV = FOV / 2

        # draw player (as a circle)
        pygame.draw.circle(window, PlayerConstants.PLAYER_COLOR, (
            self.position_x, self.position_y), self.radius)

        # draw player direction
        pygame.draw.line(window, (0, 255, 0),
                         (self.position_x, self.position_y),
                         (self.position_x - math.sin(self.player_angle) * 50,
                          self.position_y + math.cos(self.player_angle) * 50),
                         width=3)

        # draw player FOV
        # leftmost side
        pygame.draw.line(window, (0, 255, 0),
                         (self.position_x, self.position_y),
                         (self.position_x - math.sin(self.player_angle - HALF_FOV) * 50,
                          self.position_y + math.cos(self.player_angle - HALF_FOV) * 50),
                         width=3)
        # rightmost side
        pygame.draw.line(window, (0, 255, 0),
                         (self.position_x, self.position_y),
                         (self.position_x - math.sin(self.player_angle + HALF_FOV) * 50,
                          self.position_y + math.cos(self.player_angle + HALF_FOV) * 50),
                         width=3)
