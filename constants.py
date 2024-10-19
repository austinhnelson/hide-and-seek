# Display
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

# Colors
BORDER_COLOR = (100, 100, 100)  # gray
TILE_COLOR = (118, 169, 227)  # light blue

# Map
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
TILE_WIDTH = int(SCREEN_WIDTH / MAP_WIDTH)
TILE_HEIGHT = int(SCREEN_HEIGHT / MAP_HEIGHT)
