import pygame
from config import DISPLAY


class Menu:
    def __init__(self, client):
        self.client = client
        pygame.font.init()

        original_image = pygame.image.load(
            "client/assets/menu_bg.png").convert_alpha()
        self.menu_image = pygame.transform.scale(
            original_image, (DISPLAY["WIDTH"], DISPLAY["HEIGHT"]))

        self.font = pygame.font.Font(None, 36)

        self.buttons = [
            {"text": "Join Lobby", "position": (DISPLAY["WIDTH"] // 2, 395)},
            {"text": "How to Play", "position": (DISPLAY["WIDTH"] // 2, 475)},
            {"text": "Exit", "position": (DISPLAY["WIDTH"] // 2, 550)}
        ]

    def draw_menu(self, window):
        window.blit(self.menu_image, (0, 0))

        for button in self.buttons:
            text_surface = self.font.render(
                button["text"], True, (0, 0, 0))

            text_rect = text_surface.get_rect(center=button["position"])
            window.blit(text_surface, text_rect)
