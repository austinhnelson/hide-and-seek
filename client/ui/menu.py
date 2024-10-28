import pygame
from config import DISPLAY


class Menu:
    def __init__(self, client):
        self.client = client
        self.font = pygame.font.Font(None, 36)

        pygame.font.init()

    def draw(self, window):
        title = self.font.render("Game Menu", True, (255, 255, 255))
        window.blit(title, (DISPLAY["WIDTH"]//2 - title.get_width()//2, 100))

        players_text = self.font.render(
            f"Connected Players: {self.client.total_players}",
            True,
            (255, 255, 255)
        )
        window.blit(
            players_text, (DISPLAY["WIDTH"]//2 - title.get_width()//2, 200))

        y_offset = 250
        for player in self.client.player_list:
            player_text = self.font.render(
                f"Player {player['id']} - {player['address']}",
                True,
                (255, 255, 255)
            )
            window.blit(
                player_text, (DISPLAY["WIDTH"]//2 - player_text.get_width()//2, y_offset))
            y_offset += 40

        game_text = self.font.render(
            "Press SPACE to start once all players connected", True, (255, 255, 255))
        window.blit(
            game_text, (DISPLAY["WIDTH"]//2 - game_text.get_width()//2, 600))
