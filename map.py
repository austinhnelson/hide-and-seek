import pygame


class Map:
    def __init__(self, width, height, map, tile_width, tile_height, border_color, tile_color, background_color):
        self.width = width
        self.height = height
        self.map = map
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.border_color = border_color
        self.tile_color = tile_color
        self.background_color = background_color

    def draw(self, window):
        for row in range(self.height):
            for column in range(self.width):
                tile = row * self.width + column

                # draw tiles
                pygame.draw.rect(window,
                                 self.border_color if self.map[tile] == '#' else self.tile_color,
                                 (column * self.tile_width, row * self.tile_height, self.tile_width, self.tile_height))

                # draw borders for tiles
                pygame.draw.rect(window,
                                 self.background_color,
                                 (column * self.tile_width, row *
                                  self.tile_height, self.tile_width, self.tile_height),
                                 1)
