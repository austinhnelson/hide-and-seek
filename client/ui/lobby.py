import pygame
from config import DISPLAY


class Lobby:
    def __init__(self):
        pygame.font.init()

        self.font = pygame.font.Font(
            "client/assets/fonts/PlayMeGames-Demo.otf", 20)

        self.button_font = pygame.font.Font(
            "client/assets/fonts/PlayMeGames-Demo.otf", 30)

        self.image = pygame.image.load(
            "client/assets/lobby_bg.png").convert_alpha()

        self.text_box_width = 620
        self.text_box_height = 305
        self.text_box_position = (50, 300)
        self.text_padding = 20

        self.buttons = [
            {"text": "Back", "position": (
                564, 649), "selected": True},
        ]

    def draw(self, window, player_names):
        image_rect = pygame.Rect(
            550, 50, DISPLAY["WIDTH"], DISPLAY["HEIGHT"])
        window.blit(self.image, (0, 0), image_rect)

        box_rect = pygame.Rect(
            self.text_box_position[0],
            self.text_box_position[1],
            self.text_box_width,
            self.text_box_height
        )
        pygame.draw.rect(window, (255, 255, 255), box_rect, border_radius=10)
        pygame.draw.rect(window, (0, 0, 0), box_rect, 2,
                         border_radius=10)

        self.draw_player_names(window, player_names)
        self.draw_buttons(window)

    def draw_player_names(self, window, player_names):
        x, y = self.text_box_position[0] + \
            self.text_padding, self.text_box_position[1] + self.text_padding

        for name in player_names:
            name_surface = self.font.render(name, True, (0, 0, 0))
            window.blit(name_surface, (x, y))
            y += name_surface.get_height() + 5

    def draw_buttons(self, window):
        for button in self.buttons:
            text_surface = self.button_font.render(
                button["text"], True, (65, 209, 84) if button["selected"] else (0, 0, 0))
            text_rect = text_surface.get_rect(center=button["position"])
            window.blit(text_surface, text_rect)
