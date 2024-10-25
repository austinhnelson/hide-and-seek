import asyncio
import socket


class Server():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5003

        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))

        self.server_socket.listen(2)
        self.connections = []

    def get_players(self):
        return self.connections

    async def wait_for_players(self):
        while True:
            conn, address = await asyncio.to_thread(self.server_socket.accept)
            print(f"Player connected from {address}")
            self.connections.append(conn)
