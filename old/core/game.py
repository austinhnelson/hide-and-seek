import asyncio
import math
import sys
import pygame

from config import DISPLAY, MAP, TILE, NETWORK
from core.input_manager import InputManager
from network import Server
from graphics import RayCasting
from entities import Map, Player
from ui import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode(
            (DISPLAY["WIDTH"], DISPLAY["HEIGHT"]))
        pygame.display.set_caption(DISPLAY["CAPTION"])
        self.clock = pygame.time.Clock()

        self.server = Server()
        self.menu = Menu(self.server)
        self.map = Map()
        self.player = Player()

        self.is_menu = True
        self.running = True

        self.loop = asyncio.new_event_loop()
        self.connect_players = self.loop.create_task(
            self.server.accept_players())

    def run(self):
        try:
            while self.running:
                self.handle_events()
                self.render()
                self.clock.tick(DISPLAY["FPS"])

                self.loop.call_soon(self.loop.stop)
                self.loop.run_forever()
        finally:
            self.shutdown()

    # TODO: Is there a cleaner way to handle events?
    # Specifically, events differing from menu screen vs game?
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        if self.is_menu:
            if len(self.server.connections) == NETWORK["NUM_OF_ALLOWED_CONNECTIONS"]:
                self.is_menu = not InputManager.is_enter_selected()
        else:
            InputManager.handle_player_input(self.player)

    def render(self):
        self.window.fill(MAP["BACKGROUND_COLOR"])
        if self.is_menu:
            self.menu.draw(self.window)
        else:
            # TODO: This is not good. Looks pretty bad visually.
            visible_tiles = RayCasting.get_visible_tiles(
                self.player.player_angle,
                math.pi / 3,
                120,
                int(MAP["WIDTH"] * TILE["WIDTH"]),
                self.player.position_x,
                self.player.position_y
            )
            self.player.draw(self.window)
            self.map.draw_visible_tiles(self.window, visible_tiles)
            self.map.draw_border(self.window)

        pygame.display.flip()

    def shutdown(self):
        self.connect_players.cancel()
        try:
            self.loop.run_until_complete(self.connect_players)
        except asyncio.CancelledError:
            print("Program closing...")

        self.loop.close()
        pygame.quit()
        sys.exit(0)
