import pygame
import random
from config import DISPLAY


class Menu:
    def __init__(self, client):
        self.client = client
        pygame.font.init()

    def draw_menu(self, window):
        print("Drawing menu!")

    def draw_lobby(self, window):
        print("Drawing lobby!")
