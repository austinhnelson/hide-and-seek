import pygame


class Lobby:
    def __init__(self):
        pygame.font.init()

        self.font = pygame.font.Font(
            "client/assets/fonts/PlayMeGames-Demo.otf", 20)

    def draw(self, window):
        window.fill((0, 255, 0))
