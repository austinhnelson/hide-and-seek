import asyncio
import socket
from dotenv import load_dotenv
import os
import json

load_dotenv()


class GameClient:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = int(os.getenv("SERVER_PORT"))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player_id = None
        self.total_players = 0
        self.player_list = []
        self._message_queue = asyncio.Queue()

    async def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            self.client_socket.setblocking(False)
            # print("Connected to game server.")
            asyncio.create_task(self.receive_messages())
        except Exception as e:
            print(f"Connection error: {e}")

    async def receive_messages(self):
        while True:
            try:
                data = await asyncio.to_thread(self.client_socket.recv, 1024)
                if not data:
                    break

                try:
                    message = json.loads(data.decode())
                    await self._message_queue.put(message)
                except json.JSONDecodeError:
                    print("Invalid JSON received")

            except BlockingIOError:
                await asyncio.sleep(0.1)
            except Exception as e:
                # print(f"Error receiving message: {e}")
                break

    async def get_next_message(self):
        try:
            message = await asyncio.wait_for(self._message_queue.get(), timeout=0.1)
            return message
        except asyncio. TimeoutError:
            return None

    async def process_server_messages(self):
        message = await self.get_next_message()
        if message:
            if message["type"] == "welcome":
                self.player_id = message["player_id"]
                self.total_players = message["total_players"]
            elif message["type"] == "player_count":
                self.total_players = message["total_players"]
                self.player_list = message["players"]

    async def disconnect(self):
        self.client_socket.close()
        # print("Disconnected from game server.")
