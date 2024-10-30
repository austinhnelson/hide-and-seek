import pygame
import random
from config import DISPLAY


class Menu:
    def __init__(self, client):
        self.client = client
        self.font_large = pygame.font.Font(None, 64)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        pygame.font.init()
        self.background_color = (30, 30, 30)  # Dark background
        self.accent_color = (100, 255, 100)   # Bright accent color
        self.pulse = 0

    def draw_gradient_background(self, window):
        for y in range(0, DISPLAY["HEIGHT"], 10):
            color = (
                self.background_color[0] + (y * 1) % 50,
                self.background_color[1] + (y * 1) % 50,
                self.background_color[2] + (y * 1) % 50,
            )
            pygame.draw.line(window, color, (0, y), (DISPLAY["WIDTH"], y))

    def draw(self, window):
        self.draw_gradient_background(window)

        # Title with pulsing effect
        self.pulse = (self.pulse + 1) % 255
        title_color = (
            255, 255, 255) if self.pulse < 128 else self.accent_color
        title = self.font_large.render("Game Menu", True, title_color)
        window.blit(title, (DISPLAY["WIDTH"]//2 - title.get_width()//2, 100))

        # Connected players count with shadow
        players_text = self.font_medium.render(
            f"Connected Players: {self.client.total_players}",
            True,
            self.accent_color
        )
        window.blit(
            players_text, (DISPLAY["WIDTH"]//2 - players_text.get_width()//2, 200))

        # Display each player with animated accent
        y_offset = 250
        for player in self.client.player_list:
            player_color = (
                min(255, max(0, self.accent_color[0])),
                min(255, max(
                    0, self.accent_color[1] + random.randint(-20, 20))),
                min(255, max(
                    0, self.accent_color[2] + random.randint(-20, 20))),
            )
            player_text = self.font_medium.render(
                f"Player {player['id']} - {player['address']}",
                True,
                player_color
            )
            window.blit(
                player_text, (DISPLAY["WIDTH"]//2 - player_text.get_width()//2, y_offset))
            y_offset += 40

        # Interactive Start Game message
        game_text = self.font_small.render(
            "Press SPACE to start once all players connected", True, self.accent_color
        )
        window.blit(
            game_text, (DISPLAY["WIDTH"]//2 - game_text.get_width()//2, 600))
