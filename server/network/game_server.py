import json
import signal
import sys
import threading
import socket
import time
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
        self.running = True
        # print(f"Server successfully started on {self.port}")

        self.running_id_count = 0
        self.clients = []
        self.player_data = {
            "player_count": 0,
            "players": []
        }

        threading.Thread(target=self.__broadcast_loop, daemon=True).start()

        signal.signal(signal.SIGINT, self.__handle_shutdown)

    def run(self):
        while self.running:
            client_socket, addr = self.server.accept()
            # print(f"New connection from {addr}")
            self.clients.append(client_socket)

            self.running_id_count += 1
            player_id = self.running_id_count

            player_info = {"player_id": player_id}
            client_socket.send(json.dumps(player_info).encode('utf-8'))

            self.player_data["player_count"] += 1
            self.player_data["players"].append(
                {
                    "id": player_id,
                    "name": f"Player {player_id}",
                    "ready": False
                })

            threading.Thread(target=self.__handle_client,
                             args=(client_socket, player_id),  daemon=True).start()

    def __handle_client(self, client_socket, player_id):
        try:
            while True:
                msg = client_socket.recv(1024).decode('utf-8')
                if not msg:
                    break

                message = json.loads(msg)

                if message["type"] == "toggle_ready":
                    for player in self.player_data["players"]:
                        if player["id"] == player_id:
                            player["ready"] = message["ready"]
                            break

        except Exception as ex:
            # print(f"Error in client communication: {ex}")
            pass
        finally:
            # print(f"Client {player_id} disconnected")
            try:
                self.clients.remove(client_socket)
            except ValueError:
                pass
            self.player_data["players"] = [
                player for player in self.player_data["players"] if player["id"] != player_id
            ]

            self.player_data["player_count"] -= 1
            client_socket.close()

    def __broadcast_loop(self):
        while self.running:
            self.__broadcast(self.player_data)
            time.sleep(0.1)

    def __broadcast(self, data):
        for client in self.clients:
            try:
                client.send(json.dumps(data).encode('utf-8'))
            except Exception as ex:
                # print(f"Error sending data to client: {ex}")
                pass

    def __handle_shutdown(self, signum, frame):
        self.running = False

        for client in self.clients:
            client.close()

        self.server.close()
        sys.exit(0)
