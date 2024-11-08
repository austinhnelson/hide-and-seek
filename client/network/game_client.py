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

        self.player_data = None

        threading.Thread(target=self.__receive_data).start()

    def __receive_data(self):
        try:
            while True:
                msg = self.server.recv(1024).decode('utf-8')
                if msg:
                    self.player_data = json.load(msg)
                else:
                    # print("Server closed connection.")
                    break
        except Exception as ex:
            print(f"Error receiving data: {ex}")
        finally:
            self.__close()

    def __close(self):
        self.server.close()
