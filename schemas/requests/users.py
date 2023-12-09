from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    id_vk: int
    firstname: str
    lastname: str
