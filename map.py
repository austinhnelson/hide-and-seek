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
        # Create a temporary surface with per-pixel alpha (RGBA)
        tile_surface = pygame.Surface(
            (self.tile_width, self.tile_height), pygame.SRCALPHA)

        # Set the color with alpha (opacity) included
        for col, row in tiles:
            # Fill the surface with the tile color including alpha
            # tile_color should be (R, G, B, A)
            tile_surface.fill(self.tile_color)

            # Blit the tile surface with transparency onto the main window
            window.blit(tile_surface, (col * self.tile_width,
                        row * self.tile_height))
