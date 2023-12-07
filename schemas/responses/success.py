from typing import List

from pydantic import BaseModel


class Success(BaseModel):
    success: bool
    description: List[str] = []


class CreateRoomSuccess(Success):
    id: int
