from typing import List, Union
from pydantic import BaseModel


class RoomSchema(BaseModel):
    id: int
    name: str
    password: Union[int, None]


class ListRoomSchema(BaseModel):
    rooms: List[RoomSchema]
