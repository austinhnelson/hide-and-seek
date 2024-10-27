import socket
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


class GameServer:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = int(os.getenv("SERVER_PORT"))
        self.player_connections = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(int(os.getenv("ALLOWED_CONNECTIONS")))
        print(f"Server successfully started on {self.port}")

    async def listen_for_connections(self):
        while True:
            conn, addr = await asyncio.to_thread(self.server_socket.accept)
            self.player_connections.append(conn)
            print(f"Player connected from {addr}")

    async def run(self):
        await self.listen_for_connections()
