import pygame
from constants import MAP_WIDTH, MAP_HEIGHT, MAP, TILE_WIDTH, TILE_HEIGHT, BORDER_COLOR, TILE_COLOR


class Map:
    def __init__(self) -> None:
        pass

    def draw_map(self, window):
        for row in range(MAP_WIDTH):
            for column in range(MAP_HEIGHT):
                square = row * MAP_WIDTH + column
                pygame.draw.rect(window,
                                 BORDER_COLOR if MAP[square] == '#' else TILE_COLOR,
                                 (row * TILE_WIDTH, column * TILE_HEIGHT, TILE_WIDTH - 2, TILE_HEIGHT - 2))
