from sqlalchemy.orm import Session

from constants.constants import MAX_ON_PAGE
from models.models import Friends, Room, RoomUser, User
from schemas.responses.rooms import (
    InventSchema,
    NameRoomsSchema,
    ListFrienRoomsSchema,
    ListRoomSchema,
    RoomSchema,
)


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


def friend_rooms_view(id_vk: int, page: int, db: Session):
    friend_rooms = (
        db.query(
            User.id,
            User.firstname,
            User.lastname,
            Room.id,
            Room.name,
            Room.password,
        )
        .select_from(Friends)
        .join(User, Friends.user2_id == User.id)
        .join(RoomUser, Friends.user2_id == RoomUser.user_id)
        .join(Room, RoomUser.room_id == Room.id)
        .filter(Friends.user1_id == id_vk)
        .order_by(User.lastname)
        .offset(page * MAX_ON_PAGE)
        .limit(MAX_ON_PAGE)
    )

    if friend_rooms:
        previous_name = f"{friend_rooms[0][1]} {friend_rooms[0][2]}"

    friends = []
    rooms = []
    for row in friend_rooms:
        user_name = f"{row[1]} {row[2]}"

        name_password = RoomSchema(
            id=row[3],
            name=row[4],
            password=row[5],
        )

        if user_name != previous_name:
            friends.append(
                NameRoomsSchema(
                    name=user_name,
                    rooms=rooms,
                )
            )
            rooms = []

        rooms.append(name_password)
        previous_name = user_name

    friends.append(
        NameRoomsSchema(
            name=user_name,
            rooms=rooms,
        )
    )

    return ListFrienRoomsSchema(friends=friends)


def invent_view(id_vk: int, room_id: int, db: Session):
    room = (
        db.query(RoomUser.invent)
        .filter(RoomUser.user_id == id_vk, RoomUser.room_id == room_id)
        .first()
    )

    return InventSchema(invent=room[0])
