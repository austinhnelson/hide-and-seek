import pygame
import math
from constants import *


class RayCasting:
    @staticmethod
    def get_visible_tiles(player_angle, fov, casted_rays, max_depth, position_x, position_y):
        step_angle = fov / casted_rays
        start_angle = player_angle - (fov / 2)

        visible_tiles = set()

        for ray in range(casted_rays):
            for depth in range(max_depth):
                target_x = position_x - math.sin(start_angle) * depth
                target_y = position_y + math.cos(start_angle) * depth

                col = int(target_x / MapConstants.TILE_WIDTH)
                row = int(target_y / MapConstants.TILE_HEIGHT)

                if 0 <= col < MapConstants.MAP_WIDTH and 0 <= row < MapConstants.MAP_HEIGHT:
                    visible_tiles.add((col, row))
                    square = row * MapConstants.MAP_WIDTH + col
                    if MapConstants.MAP[square] == '#':
                        break

            start_angle += step_angle
        return visible_tiles
