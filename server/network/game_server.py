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

    async def handle_client(self, conn, addr):
        print(f"Player connected from {addr}")
        try:
            while True:
                data = await asyncio.to_thread(conn.recv, 1024)
                if not data:
                    break
                print(f"Received from {addr}: {data.decode()}")
        finally:
            self.disconnect_client(conn, addr)

    async def listen_for_connections(self):
        while True:
            conn, addr = await asyncio.to_thread(self.server_socket.accept)
            self.player_connections.append(conn)
            asyncio.create_task(self.handle_client(conn, addr))

    def disconnect_client(self, conn, addr):
        print(f"Player {addr} disconnected.")
        self.player_connections.remove(conn)

    async def run(self):
        await self.listen_for_connections()
