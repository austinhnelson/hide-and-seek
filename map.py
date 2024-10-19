import pygame
from constants import MAP_WIDTH, MAP_HEIGHT, MAP, TILE_WIDTH, TILE_HEIGHT


class Map:
    def __init__(self) -> None:
        pass

    def draw_map(self, window):
        for row in range(MAP_WIDTH):
            for column in range(MAP_HEIGHT):
                square = row * 8 + column
                pygame.draw.rect(window,
                                 (200, 200, 200) if MAP[square] == '#' else (
                                     100, 100, 100),
                                 (row * TILE_WIDTH, column * TILE_HEIGHT, TILE_WIDTH - 2, TILE_HEIGHT - 2))
