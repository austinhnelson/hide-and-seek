from .base import StateBase
import pygame


class MenuState(StateBase):
    def __init__(self, menu):
        self.menu = menu

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.menu.select_down()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.menu.select_up()

    def render(self, window):
        self.menu.draw_menu(window)
