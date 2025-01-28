import pygame


class Map:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.map = (
            '########'
            '#  #   #'
            '#   #  #'
            '##     #'
            '#      #'
            '#  ##  #'
            '#     ##'
            '########'
        )
        self.tile_width = 720 // 8
        self.tile_height = 720 // 8
        self.border_color = (100, 100, 100)
        self.tile_color = (118, 169, 227)
        self.background_color = (0, 0, 0)

    def draw(self, window, players, x=None, y=None):
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

        for player in players:
            pos = player["position"]
            pygame.draw.circle(
                window,
                (255, 0, 0),
                (int(pos["x"]), int(pos["y"])),
                self.tile_width // 4
            )
