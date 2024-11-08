import pygame
from .states import MenuState
from network import GameClient


class GameState:
    def __init__(self):
        self.state = MenuState(self)
        self.running = True
        self.client = GameClient()

    def set_state(self, new_state):
        self.state = new_state

    def handle_input(self, event):
        self.state.handle_input(event)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.handle_input(event)

    def run(self):
        self.handle_events()

    def render(self, window):
        window.fill((0, 0, 0))
        self.player_list = self.client.player_list
        self.state.render(window)
        pygame.display.flip()

    async def shutdown(self):
        await self.client.disconnect()


# await self.client.process_server_messages()
# connect_task = asyncio.create_task(self.client.connect())
