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

        self.font = pygame.font.Font(
            "client/assets/fonts/PlayMeGames-Demo.otf", 20)

        self.buttons = [
            {"text": "Join Lobby", "position": (
                DISPLAY["WIDTH"] // 2, 395), "selected": True},
            {"text": "How to Play", "position": (
                DISPLAY["WIDTH"] // 2, 475), "selected": False},
            {"text": "Exit", "position": (
                DISPLAY["WIDTH"] // 2, 550), "selected": False},
        ]

    def select_down(self):
        for index, button in enumerate(self.buttons):
            if button["selected"]:
                button["selected"] = False
                next_index = (index + 1) % len(self.buttons)
                self.buttons[next_index]["selected"] = True
                break

    def select_up(self):
        for index, button in enumerate(self.buttons):
            if button["selected"]:
                button["selected"] = False
                next_index = (index - 1) % len(self.buttons)
                self.buttons[next_index]["selected"] = True
                break

    def draw_menu(self, window):
        window.blit(self.menu_image, (0, 0))

        for button in self.buttons:
            text_surface = self.font.render(
                button["text"], True, (65, 209, 84) if button["selected"] else (0, 0, 0))
            text_rect = text_surface.get_rect(center=button["position"])
            window.blit(text_surface, text_rect)

    def draw_lobby(self, window):
        window.fill((0, 0, 0))
