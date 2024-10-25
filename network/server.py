import asyncio
import socket
from config import NETWORK


class Server():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = NETWORK["SERVER_PORT"]
        self.connections = []

        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(NETWORK["NUM_OF_ALLOWED_CONNECTIONS"])

    async def accept_players(self):
        try:
            while True:
                conn, address = await asyncio.to_thread(self.server_socket.accept)
                self.connections.append(conn)
                print(f"Accepted connection from {address}")
        except asyncio.CancelledError:
            print("Accept task cancelled, closing socket.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.server_socket.close()
