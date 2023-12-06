from pydantic import BaseModel


class UserCreate(BaseModel):
    id_vk: int
    token_vk: str
    firstname: str
    lastname: str
