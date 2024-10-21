import math
import pygame
import sys
import asyncio
from constants import DisplayConstants, MapConstants, PlayerConstants
from map import Map
from player import Player
from input_manager import InputManager
from raycasting import RayCasting


async def main():
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

        InputManager.handle_player_input(player)
        RayCasting.ray_casting(window, player.player_angle, math.pi / 3,
                               120, int(MapConstants.MAP_WIDTH * MapConstants.TILE_WIDTH), player.position_x, player.position_y)
        player.draw(window)

        pygame.display.flip()
        clock.tick(30)
        await asyncio.sleep(0)

asyncio.run(main())
