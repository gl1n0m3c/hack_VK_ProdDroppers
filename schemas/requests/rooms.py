from typing import Union

from pydantic import BaseModel


class RoomCreateSchema(BaseModel):
    id_vk: int
    name: str
    password: Union[int, None]


class UserToRoomSchema(BaseModel):
    id_vk: int
    room_id: int


class UserInventSchema(BaseModel):
    invent: str
