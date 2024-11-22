from .base import StateBase
from .how_to_play import HowToPlayState
from .lobby import LobbyState
from ui import Menu
import pygame


class MenuState(StateBase):
    def __init__(self, game_state):
        self.menu = Menu()
        self.game_state = game_state

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.menu.select_down()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.menu.select_up()
            elif event.key == pygame.K_RETURN:
                self.select_option()

    def select_option(self):
        for button in self.menu.buttons:
            if button["selected"]:
                if button["text"] == "Join Lobby":
                    isConnected = self.game_state.initializeClient()
                    if isConnected:
                        self.game_state.set_state(
                            LobbyState(self.game_state))
                elif button["text"] == "How to Play":
                    self.game_state.set_state(HowToPlayState(self.game_state))
                elif button["text"] == "Exit":
                    self.game_state.running = False

    def render(self, window):
        self.menu.draw(window)
