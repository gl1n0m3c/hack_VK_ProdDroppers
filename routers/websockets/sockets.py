from typing import List
import json

from fastapi import APIRouter, WebSocket


router = APIRouter()


MANAGERS = []
error_message = {"message": ["Отсутствует ключ 'action' в данных"]}


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
            ws: WebSocket
            await ws.send_text(message)


@router.websocket("/{room_id}/")
async def chat(websocket: WebSocket, room_id: int):
    await websocket.accept()
    websocket.location = 0

    for manager in MANAGERS:
        manager: WebSocketManager
        if manager.room_id == room_id:
            await manager.connect(websocket=websocket)
            break
    else:
        manager = WebSocketManager(room_id=room_id)
        MANAGERS.append(manager)
        await manager.connect(websocket=websocket)

    try:
        while True:
            data = await websocket.receive_text()

            data_dump = json.loads(data)
            action = data_dump["action"]
            location_id = data_dump["location_id"]
            print(action, location_id)

            if action == 0:
                for ws in manager.active_connections:
                    ws: WebSocket
                    if ws.location == location_id and ws != websocket:
                        await ws.send_text(data)

            elif action == 1:
                for ws in manager.active_connections:
                    ws: WebSocket
                    if ws.location == location_id:
                        await ws.send_text(data)

            elif action == 2:
                for ws in manager.active_connections:
                    ws: WebSocket
                    if ws.location == location_id and ws != websocket:
                        await ws.send_text(data)

            elif action == 3:
                websocket.location = location_id

    except Exception:
        manager.disconnect(websocket=websocket)
