import pygame
import sys
import math
from constants import DisplayConstants, MapConstants, PlayerConstants
from map import Map
from player import Player

pygame.init()

window = pygame.display.set_mode(
    (DisplayConstants.SCREEN_WIDTH, DisplayConstants.SCREEN_HEIGHT))
pygame.display.set_caption(DisplayConstants.CAPTION)
clock = pygame.time.Clock()

map = Map(
    MapConstants.MAP_WIDTH,
    MapConstants.MAP_HEIGHT,
    MapConstants.MAP,
    MapConstants.TILE_WIDTH,
    MapConstants.TILE_HEIGHT,
    MapConstants.BORDER_COLOR,
    MapConstants.TILE_COLOR,
    MapConstants.BACKGROUND_COLOR)

player = Player(
    PlayerConstants.PLAYER_INITIAL_X,
    PlayerConstants.PLAYER_INITIAL_Y,
    PlayerConstants.PLAYER_RADIUS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    window.fill(MapConstants.BACKGROUND_COLOR)
    map.draw(window)
    player.draw(window)

    pygame.display.flip()
    clock.tick(60)
