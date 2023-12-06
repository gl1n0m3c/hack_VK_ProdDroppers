from sqlalchemy.orm import Session

from models.models import User
from schemas.requests.users import UserCreate
from schemas.responses.success import Success


def auth_controller(data: UserCreate, db: Session):
    user = db.query(User).filter(User.id_vk == data.id_vk).first()

    if user:
        return Success(
            success=True, description=["Пользователь авторизирован"]
        )

    user = User(
        id_vk=data.id_vk,
        token_vk=data.token_vk,
        firstname=data.firstname,
        lastname=data.lastname,
    )
    db.add(user)
    db.commit()

    return Success(success=True, description=["Пользователь зарегистрирован"])
