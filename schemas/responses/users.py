from typing import List

from pydantic import BaseModel


class FriendsSchema(BaseModel):
    id: int
    firstname: str
    lastname: str


class ListFriendsSchema(BaseModel):
    friends: List[FriendsSchema]


class UserSchema(BaseModel):
    id: int
    firstname: str
    lastname: str


class ListUserSchema(BaseModel):
    users: List[UserSchema]
