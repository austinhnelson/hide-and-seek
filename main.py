import math
import pygame
import sys
import asyncio
from constants import DisplayConstants, MapConstants, PlayerConstants
from map import Map
from player import Player
from input_manager import InputManager
from raycasting import RayCasting
from menu_screen import MenuScreen
from sockets.server import Server


async def main():
    pygame.init()

    window = pygame.display.set_mode(
        (DisplayConstants.SCREEN_WIDTH, DisplayConstants.SCREEN_HEIGHT))
    pygame.display.set_caption(DisplayConstants.CAPTION)
    clock = pygame.time.Clock()

    server = Server()
    menu_screen = MenuScreen(server)

    map = Map(
        MapConstants.MAP_WIDTH,
        MapConstants.MAP_HEIGHT,
        MapConstants.MAP,
        MapConstants.TILE_WIDTH,
        MapConstants.TILE_HEIGHT,
        MapConstants.BORDER_COLOR,
        MapConstants.TILE_COLOR,
        MapConstants.BACKGROUND_COLOR
    )

    player = Player(
        PlayerConstants.PLAYER_INITIAL_X,
        PlayerConstants.PLAYER_INITIAL_Y,
        PlayerConstants.PLAYER_RADIUS
    )

    isMenuScreen = True
    wait_task = asyncio.create_task(server.wait_for_players())

    try:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    break  # Break out of the loop to cleanly exit

            if isMenuScreen:
                if len(server.connections) == 2:
                    isMenuScreen = InputManager.handle_menu_input(menu_screen)

                menu_screen.draw(window)
            else:
                InputManager.handle_player_input(player)
                window.fill(MapConstants.BACKGROUND_COLOR)
                visible_tiles = RayCasting.get_visible_tiles(
                    player.player_angle,
                    math.pi / 3,
                    120,
                    int(MapConstants.MAP_WIDTH * MapConstants.TILE_WIDTH),
                    player.position_x,
                    player.position_y
                )
                player.draw(window)
                map.draw_tiles(window, visible_tiles)
                map.draw_border(window)

            pygame.display.flip()
            clock.tick(30)
            await asyncio.sleep(0)
    finally:
        wait_task.cancel()  # Cancel the wait task
        await wait_task  # Wait for the task to finish if needed
        pygame.quit()
        sys.exit(0)

asyncio.run(main())
