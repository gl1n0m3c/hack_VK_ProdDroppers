from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    id_vk: int
    firstname: str
    lastname: str


class ChangeInventSchema(BaseModel):
    id_vk: int
    room_id: int
    invent: str
