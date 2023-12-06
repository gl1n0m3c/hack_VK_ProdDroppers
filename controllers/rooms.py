from sqlalchemy.orm import Session

from constants.constants import MAX_ROOMS
from models.models import Room, RoomUser, User
from schemas.requests.rooms import RoomCreateSchema, UserToRoomSchema
from schemas.responses.success import Success


def rooms(id: int, db: Session):
    number_of_rooms = (
        db.query(RoomUser).join(User).filter(User.id == id).count()
    )

    if number_of_rooms == MAX_ROOMS:
        return Success(
            success=False,
            description=[
                f"Вы уже имеете {MAX_ROOMS} активные комнаты, "
                "удалите 1 существующую, "
                "чтобы создать новую"
            ],
        )
    return True


def create_room_controller(data: RoomCreateSchema, db: Session):
    user = db.query(User).filter(User.id == data.id_vk).count()
    if user == 0:
        return Success(
            success=False,
            description=["Такого пользователя не существует!"],
        )

    resault = rooms(id=data.id_vk, db=db)
    if resault == True:
        new_room = Room(
            name=data.name,
            password=data.password,
        )

        db.add(new_room)
        db.commit()

        new_room = (
            db.query(Room)
            .filter_by(name=data.name, password=data.password)
            .first()
        )

        new_room_user = RoomUser(
            user_id=data.id_vk,
            room_id=new_room.id,
        )

        db.add(new_room_user)
        db.commit()

        return Success(success=True)
    return resault


def user_to_room_controller(data: UserToRoomSchema, db: Session):
    room = (
        db.query(RoomUser)
        .filter(
            RoomUser.user_id == data.id_vk,
            RoomUser.room_id == data.room_id,
        )
        .first()
    )

    if room:
        return Success(success=True)

    resault = rooms(id=data.id_vk, db=db)
    if resault == True:
        room = RoomUser(
            user_id=data.id_vk,
            room_id=data.room_id,
        )

        db.add(room)
        db.commit()
        return Success(success=True)
    return resault
