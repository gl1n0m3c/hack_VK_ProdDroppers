from pydantic import BaseModel


class FriendsSchema(BaseModel):
    id1_vk: int
    id2_vk: int
