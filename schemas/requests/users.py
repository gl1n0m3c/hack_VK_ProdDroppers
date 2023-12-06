from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    id_vk: int
    token_vk: str
    firstname: str
    lastname: str
