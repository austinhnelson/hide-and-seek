import json
import socket
from dotenv import load_dotenv
import os
import threading

load_dotenv()


class GameClient:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = int(os.getenv("SERVER_PORT"))
        self.server.connect((self.host, self.port))

        self.ready = False

        player_info = json.loads(self.server.recv(1024).decode('utf-8'))
        self.client_id = player_info["player_id"]

        self.player_data = {
            "player_count": 0,
            "players": []
        }

        threading.Thread(target=self.receive_data).start()

    def receive_data(self):
        try:
            while True:
                msg = self.server.recv(1024).decode('utf-8')
                if msg:
                    self.player_data = json.loads(msg)
                else:
                    print("Server closed connection.")
                    break
        except Exception as ex:
            print(f"Error receiving data: {ex}")
        finally:
            self.close()

    def toggle_ready(self):
        self.ready = not self.ready

        message = {
            "type": "toggle_ready",
            "player_id": self.client_id,
            "ready": self.ready
        }

        try:
            self.server.send(json.dumps(message).encode('utf-8'))
        except Exception as ex:
            print(f"Failed to send message to server: {ex}")

    def update_position(self, x, y):
        message = {
            "type": "update_position",
            "position": {
                "x": x,
                "y": y,
            }
        }

        try:
            self.server.send(json.dumps(message).encode('utf-8'))
        except Exception as ex:
            print(f"Failed to send message to server: {ex}")

    def close(self):
        self.server.close()
