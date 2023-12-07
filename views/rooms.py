from sqlalchemy.orm import Session

from constants.constants import MAX_ON_PAGE
from models.models import Room
from schemas.responses.rooms import ListRoomSchema, RoomSchema


def all_rooms_view(page: int, db: Session):
    rooms = db.query(Room).offset(page * MAX_ON_PAGE).limit(MAX_ON_PAGE)

    rooms_data = [
        RoomSchema(
            id=room_data.id,
            name=room_data.name,
            password=room_data.password,
        )
        for room_data in rooms
    ]

    return ListRoomSchema(rooms=rooms_data)
