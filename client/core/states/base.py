from abc import ABC, abstractmethod


class StateBase(ABC):
    @abstractmethod
    def handle_input(self, event):
        pass

    @abstractmethod
    def render(self, window):
        pass
