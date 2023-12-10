from sqlalchemy.orm import Session

from models.models import RoomUser, User
from schemas.requests.users import ChangeInventSchema, UserCreateSchema
from schemas.responses.success import Success


def auth_controller(data: UserCreateSchema, db: Session):
    user = db.query(User).filter(User.id == data.id_vk).first()

    if user:
        return Success(
            success=True,
            description=["Пользователь авторизирован"],
        )

    user = User(
        id=data.id_vk,
        firstname=data.firstname,
        lastname=data.lastname,
    )
    db.add(user)
    db.commit()

    return Success(success=True, description=["Пользователь зарегистрирован"])


def сhange_invent_controller(data: ChangeInventSchema, db: Session):
    user = (
        db.query(RoomUser)
        .filter_by(
            user_id=data.id_vk,
            room_id=data.room_id,
        )
        .first()
    )

    if user:
        user.invent = data.invent
        db.commit()

    return Success(success=True)
