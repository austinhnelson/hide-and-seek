import json
import socket
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


class GameServer:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = int(os.getenv("SERVER_PORT"))
        self.player_connections = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(int(os.getenv("ALLOWED_CONNECTIONS")))
        print(f"Server successfully started on {self.port}")

    async def handle_client(self, conn, addr):
        player_id = len(self.player_connections) + 1
        self.player_connections[addr] = {
            "connection": conn,
            "player_id": player_id
        }
        print(f"Player {player_id} connected from {addr}")

        welcome_message = {
            "type": "welcome",
            "player_id": player_id,
            "total_players": len(self.player_connections)
        }
        await asyncio.to_thread(conn.send, json.dumps(welcome_message).encode())

        await asyncio.sleep(0.05)
        await self.broadcast_player_count()

        try:
            while True:
                data = await asyncio.to_thread(conn.recv, 1024)
                if not data:
                    break
        except (ConnectionResetError, BrokenPipeError):
            print(f"Player {addr} unexpectedly disconnected.")
        finally:
            await self.disconnect_client(conn, addr)

    async def broadcast_player_count(self):
        message = {
            "type": "player_count",
            "total_players": len(self.player_connections),
            "players": [
                {"id": info["player_id"], "address": str(addr)}
                for addr, info in self.player_connections.items()
            ]
        }
        for info in self.player_connections.values():
            try:
                await asyncio.to_thread(info["connection"].send, json.dumps(message).encode())
            except:
                continue

    async def listen_for_connections(self):
        while True:
            conn, addr = await asyncio.to_thread(self.server_socket.accept)
            asyncio.create_task(self.handle_client(conn, addr))

    async def disconnect_client(self, conn, addr):
        if addr in self.player_connections:
            player_id = self.player_connections[addr]["player_id"]
            print(f"Player {player_id} from {addr} disconnected.")
            del self.player_connections[addr]
            await self.broadcast_player_count()
        conn.close()

    async def run(self):
        await self.listen_for_connections()
