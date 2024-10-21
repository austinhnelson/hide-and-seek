import pygame
import math
from constants import *


class RayCasting:
    @staticmethod
    def ray_casting(window, player_angle, fov, casted_rays, max_depth, position_x, position_y):
        step_angle = fov / casted_rays
        start_angle = player_angle - (fov / 2)

        for ray in range(casted_rays):
            for depth in range(max_depth):
                target_x = position_x - math.sin(start_angle) * depth
                target_y = position_y + math.cos(start_angle) * depth

                col = int(target_x / MapConstants.TILE_WIDTH)
                row = int(target_y / MapConstants.TILE_HEIGHT)

                square = row * MapConstants.MAP_WIDTH + col
                if MapConstants.MAP[square] == '#':
                    pygame.draw.rect(window, (0, 255, 0), (col * MapConstants.TILE_HEIGHT,
                                                           row * MapConstants.TILE_WIDTH,
                                                           MapConstants.TILE_HEIGHT - 2,
                                                           MapConstants.TILE_WIDTH - 2))
                    pygame.draw.line(window, (0, 255, 0),
                                     (position_x, position_y),
                                     (target_x, target_y))
                    break
            start_angle += step_angle
