from shared.constants import NETWORK
import socket
import asyncio


class GameServer:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = NETWORK["SERVER_PORT"]
        self.player_connections = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(NETWORK["ALLOWED_CONNECTIONS"])

    async def listen_for_connections(self):
        while True:
            conn, addr = await asyncio.to_thread(self.server_socket.accept)
            self.player_connections.append(conn)
            print(f"Player connected from {addr}")

    async def run(self):
        await self.listen_for_connections()
