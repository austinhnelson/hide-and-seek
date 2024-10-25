import pygame
from config import MAP, TILES


class Map:
    def __init__(self):
        self.width = MAP["WIDTH"]
        self.height = MAP["HEIGHT"]
        self.map = MAP["BOARD"]
        self.tile_width = TILES["WIDTH"]
        self.tile_height = TILES["HEIGHT"]
        self.border_color = MAP["BORDER_COLOR"]
        self.tile_color = TILES["COLOR"]
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

    def draw_tiles(self, window, tiles):
        tile_surface = pygame.Surface(
            (self.tile_width, self.tile_height), pygame.SRCALPHA)

        for col, row in tiles:
            tile_surface.fill(self.tile_color)

            window.blit(tile_surface, (col * self.tile_width,
                        row * self.tile_height))
