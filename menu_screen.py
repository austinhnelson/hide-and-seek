import pygame
from constants import *


class MenuScreen:
    def __init__(self, server):
        pygame.font.init()
        self.my_font = pygame.font.SysFont(None, 30)
        self.text_color = (255, 0, 0)
        self.server = server

    def draw(self, window):
        player_addresses = self.server.get_players()

        for index, conn in enumerate(player_addresses):
            address = conn.getpeername()
            text_surface = self.my_font.render(
                f"Player {index + 1}: {address[0]}:{address[1]}", True, self.text_color)

            # Position the text
            text_rect = text_surface.get_rect(
                center=(DisplayConstants.SCREEN_WIDTH / 2, DisplayConstants.SCREEN_HEIGHT / 2 + index * 30))

            window.blit(text_surface, text_rect)

        color = (0, 255, 0) if len(
            self.server.connections) >= 2 else (255, 0, 0)
        pygame.draw.rect(window, color, (300, 500, 100, 100))
