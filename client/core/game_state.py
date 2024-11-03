from .states import MenuState


class GameState:
    def __init__(self, menu):
        self.state = MenuState(menu)

    def set_state(self, new_state):
        self.state = new_state

    def handle_input(self, event):
        self.state.handle_input(event)

    def render(self, window):
        self.state.render(window)
