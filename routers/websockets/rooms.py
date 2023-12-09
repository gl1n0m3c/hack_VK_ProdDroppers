import asyncio
from os import name
from typing import List

from fastapi import APIRouter, WebSocket


router = APIRouter()


MANAGERS = []


class WebSocketManager:
    def __init__(self, room_id: int):
        self.active_connections: List[WebSocket] = []
        self.room_id = room_id

    async def connect(self, websocket: WebSocket):
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_to_group(self, message: str):
        for ws in self.active_connections:
            await ws.send_text(message)


@router.websocket("/{room_id}/")
async def chat(websocket: WebSocket, room_id: int):
    await websocket.accept()

    for manager in MANAGERS:
        manager: WebSocketManager
        if manager.room_id == room_id:
            await manager.connect(websocket=websocket)
            break
    else:
        manager = WebSocketManager(room_id=room_id)
        await manager.connect(websocket=websocket)
        MANAGERS.append(manager)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_to_group(message=f"Message text was: {data}")
    except Exception:
        manager.disconnect(websocket=websocket)
