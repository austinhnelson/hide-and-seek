DISPLAY = {
    "WIDTH": 720,
    "HEIGHT": 720,
    "CAPTION": "Hide & Seek",
    "FPS": 30
}

MAP = {
    "WIDTH": 8,
    "HEIGHT": 8,
    "BOARD": (
        '########'
        '#  #   #'
        '#   #  #'
        '##     #'
        '#      #'
        '#  ##  #'
        '#     ##'
        '########'
    ),
    "BORDER_COLOR": (100, 100, 100, 255),
    "BACKGROUND_COLOR": (0, 0, 0, 255),
}

TILES = {
    "WIDTH": DISPLAY["WIDTH"] // MAP["WIDTH"],
    "HEIGHT": DISPLAY["HEIGHT"] // MAP["HEIGHT"],
    "COLOR": (118, 169, 227, 128),
}

PLAYER = {
    "INITIAL_X": DISPLAY["WIDTH"] // 2,
    "INITIAL_Y": DISPLAY["HEIGHT"] // 2,
    "RADIUS": 8,
    "COLOR": (255, 0, 0),
}

NETWORK = {
    "SERVER_PORT": 5003,
    "NUM_OF_ALLOWED_CONNECTIONS": 2,
}
