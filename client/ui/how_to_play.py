import pygame
from config import DISPLAY


class HowToPlay:
    def __init__(self):
        pygame.font.init()

        self.image = pygame.image.load(
            "client/assets/sky_bg.png").convert_alpha()

        self.font = pygame.font.Font(
            "client/assets/fonts/KodeMono-VariableFont_wght.ttf", 20)
        self.button_font = pygame.font.Font(
            "client/assets/fonts/PlayMeGames-Demo.otf", 30)
        self.text = [
            "             Welcome to Hide and Seek",
            "",
            "In this game, you will be selected as either a",
            "hider or a seeker. If you're a seeker, your",
            "objective is to seek out other players and",
            "keep them in your FOV in order to deal damage.",
            "If you're selected as a hider, stay out of the",
            "seeker's FOV and be the last one left alive!",
            "Pick up health packs to regain missing health.",
            "Use WASD or arrow keys to move around.",
            "",
            "Head back to the menu and join a lobby",
            "to get started!"
        ]

        self.text_box_width = 620
        self.text_box_height = 420
        self.text_box_position = (50, 80)
        self.text_padding = 20

        self.buttons = [
            {"text": "Back", "position": (
                557, 545), "selected": True},
        ]

    def draw_text_box(self, window):
        image_rect = pygame.Rect(550, 100, DISPLAY["WIDTH"], DISPLAY["HEIGHT"])
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

        for i, line in enumerate(self.text):
            text_surface = self.font.render(line, True, (0, 0, 0))
            window.blit(
                text_surface,
                (
                    self.text_box_position[0] + self.text_padding,
                    self.text_box_position[1] + self.text_padding + i * 30
                )
            )

    def draw_buttons(self, window):
        for button in self.buttons:
            text_surface = self.button_font.render(
                button["text"], True, (65, 209, 84) if button["selected"] else (0, 0, 0))
            text_rect = text_surface.get_rect(center=button["position"])
            window.blit(text_surface, text_rect)

    def draw(self, window):
        self.draw_text_box(window)
        self.draw_buttons(window)
