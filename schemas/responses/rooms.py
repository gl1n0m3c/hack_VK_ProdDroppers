from typing import List, Union
from pydantic import BaseModel


class RoomSchema(BaseModel):
    id: int
    name: str
    password: Union[int, None]


class ListRoomSchema(BaseModel):
    rooms: List[RoomSchema]


class NameRoomsSchema(BaseModel):
    name: str
    rooms: List[RoomSchema]


class ListFrienRoomsSchema(BaseModel):
    friends: List[NameRoomsSchema]


class InventSchema(BaseModel):
    invent: str
