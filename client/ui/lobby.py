import pygame
from config import DISPLAY


class Lobby:
    def __init__(self):
        pygame.font.init()

        self.font = pygame.font.Font(
            "client/assets/fonts/PlayMeGames-Demo.otf", 20)

        self.image = pygame.image.load(
            "client/assets/lobby_bg.png").convert_alpha()

    def draw(self, window):
        image_rect = pygame.Rect(
            550, 50, DISPLAY["WIDTH"], DISPLAY["HEIGHT"])
        window.blit(self.image, (0, 0), image_rect)
