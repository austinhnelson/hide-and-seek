import pygame
from config import DISPLAY


class Menu:
    def __init__(self, server):
        pygame.font.init()
        self.my_font = pygame.font.SysFont(None, 30)
        self.text_color = (255, 0, 0)
        self.server = server

    # TODO: Thing is hideous, need to update this.
    def draw(self, window):
        player_addresses = self.server.connections

        for index, conn in enumerate(player_addresses):
            address = conn.getpeername()
            text_surface = self.my_font.render(
                f"Player {index + 1}: {address[0]}:{address[1]}", True, self.text_color)

            text_rect = text_surface.get_rect(
                center=(DISPLAY["WIDTH"] / 2, DISPLAY["HEIGHT"] / 2 + index * 30))

            window.blit(text_surface, text_rect)

        color = (0, 255, 0) if len(
            self.server.connections) >= 2 else (255, 0, 0)
        pygame.draw.rect(window, color, (300, 500, 100, 100))
