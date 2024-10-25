import pygame
from config import MAP, TILE


class Map:
    def __init__(self):
        self.width = MAP["WIDTH"]
        self.height = MAP["HEIGHT"]
        self.map = MAP["BOARD"]
        self.tile_width = TILE["WIDTH"]
        self.tile_height = TILE["HEIGHT"]
        self.border_color = MAP["BORDER_COLOR"]
        self.tile_color = TILE["COLOR"]
        self.background_color = MAP["BACKGROUND_COLOR"]

    def draw_border(self, window):
        for row in range(self.height):
            for column in range(self.width):
                tile = row * self.width + column
                if (self.map[tile] == '#'):
                    # draw tiles
                    pygame.draw.rect(window,
                                     self.border_color,
                                     (column * self.tile_width, row * self.tile_height, self.tile_width, self.tile_height))

                    # draw borders for tiles
                    pygame.draw.rect(window,
                                     self.background_color,
                                     (column * self.tile_width, row *
                                      self.tile_height, self.tile_width, self.tile_height),
                                     1)

    def draw_visible_tiles(self, window, tiles):
        for col, row in tiles:
            pygame.draw.rect(window, self.tile_color,
                             (col * self.tile_width, row * self.tile_height,
                              self.tile_width, self.tile_height))
