from .base import StateBase
from .lobby import LobbyState
import pygame


class MenuState(StateBase):
    def __init__(self, menu, game_state):
        self.menu = menu
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
                    print("this would transition the game into lobby")
                elif button["text"] == "How to Play":
                    print("this would transition the game into how to play")
                elif button["text"] == "Exit":
                    self.game_state.running = False

    def render(self, window):
        self.menu.draw_menu(window)
