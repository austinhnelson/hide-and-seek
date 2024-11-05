from .base import StateBase
from ui import HowToPlay
import pygame


class HowToPlayState(StateBase):
    def __init__(self, game_state):
        self.menu = HowToPlay()
        self.game_state = game_state

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                from .menu import MenuState
                self.game_state.set_state(MenuState(self.game_state))

    def render(self, window):
        self.menu.draw(window)
