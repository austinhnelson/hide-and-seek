class DisplayConstants:
    SCREEN_WIDTH = 720
    SCREEN_HEIGHT = 720
    CAPTION = "2D Raycasting"


class MapConstants:
    MAP_WIDTH = 8
    MAP_HEIGHT = 8
    MAP = (
        '########'
        '#  #   #'
        '#   #  #'
        '##     #'
        '#      #'
        '#  ##  #'
        '#     ##'
        '########'
    )
    TILE_WIDTH = DisplayConstants.SCREEN_WIDTH // MAP_WIDTH
    TILE_HEIGHT = DisplayConstants.SCREEN_HEIGHT // MAP_HEIGHT

    BORDER_COLOR = (100, 100, 100, 255)  # gray, fully opaque
    TILE_COLOR = (118, 169, 227, 128)  # light blue with 50% opacity
    BACKGROUND_COLOR = (0, 0, 0, 255)  # black, fully opaque


class PlayerConstants:
    PLAYER_COLOR = (255, 0, 0)  # red
    PLAYER_INITIAL_X = DisplayConstants.SCREEN_WIDTH // 2
    PLAYER_INITIAL_Y = DisplayConstants.SCREEN_HEIGHT // 2
    PLAYER_RADIUS = 8
