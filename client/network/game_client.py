import socket
from dotenv import load_dotenv
import os

load_dotenv()


class GameClient:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = int(os.getenv("SERVER_PORT"))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    async def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to game server.")
        except Exception as e:
            print(f"Connection error: {e}")

    async def disconnect(self):
        self.client_socket.close()
        print("Disconnected from game server.")
