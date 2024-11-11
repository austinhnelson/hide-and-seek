import json
import threading
import socket
from dotenv import load_dotenv
import os

load_dotenv()


class GameServer:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = int(os.getenv("SERVER_PORT"))
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(int(os.getenv("ALLOWED_CONNECTIONS")))
        # print(f"Server successfully started on {self.port}")

        self.running_total = 1
        self.clients = []
        self.player_data = {
            "player_count": 0,
            "players": []
        }

    def run(self):
        while True:
            client_socket, addr = self.server.accept()
            print(f"New connection from {addr}")
            self.clients.append(client_socket)
            self.player_data["player_count"] += 1
            self.player_data["players"].append(
                {
                    "id": self.player_data["player_count"],
                    "name": f"Player {self.player_data['player_count']}"
                })
            threading.Thread(target=self.__handle_client,
                             args=(client_socket,)).start()

    def __handle_client(self, client_socket):
        while True:
            try:
                msg = client_socket.recv(1024).decode('utf-8')
                if msg:
                    for other_client in self.clients:
                        if other_client != client_socket:
                            other_client.send(json.dumps(
                                self.player_data).encode('utf-8'))
                else:
                    break
            except:
                break

        # print(f"Client {client_socket} disconnected")
        self.clients.remove(client_socket)
        self.player_data["player_count"] -= 1
        # self.player_data["players"].remove(
        #     {
        #         "id": self.player_data["player_count"],
        #         "name": f"Player {self.player_data['player_count']}"
        #     }
        # )
        client_socket.close()
