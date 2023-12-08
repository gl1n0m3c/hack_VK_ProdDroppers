from sqlalchemy.orm import Session

from models.models import Friends, Waiters
from schemas.requests.friends import FriendsSchema
from schemas.responses.success import Success


def send_controller(data: FriendsSchema, db: Session):
    is_waiter = (
        db.query(Waiters)
        .filter_by(
            user1_id=data.id1_vk,
            user2_id=data.id2_vk,
        )
        .first()
    )

    is_sender = (
        db.query(Waiters)
        .filter_by(
            user1_id=data.id2_vk,
            user2_id=data.id1_vk,
        )
        .first()
    )

    is_friend = (
        db.query(Friends)
        .filter_by(
            user1_id=data.id1_vk,
            user2_id=data.id2_vk,
        )
        .first()
    )

    if is_waiter:
        return Success(
            success=False,
            description=["Вы уже отправили заявку этому пользователю!"],
        )

    if is_sender:
        return Success(
            success=False,
            description=["Этот пользователь уже отправил вам заявку!"],
        )

    if is_friend:
        return Success(
            success=False,
            description=["Этот пользователь уже является вашим другом!"],
        )

    send = Waiters(
        user1_id=data.id1_vk,
        user2_id=data.id2_vk,
    )

    db.add(send)
    db.commit()

    return Success(success=True)


def accept_reject_controller(data: FriendsSchema, db: Session, method: str):
    is_waiter = (
        db.query(Waiters)
        .filter_by(
            user1_id=data.id1_vk,
            user2_id=data.id2_vk,
        )
        .first()
    )

    if is_waiter:
        db.delete(is_waiter)
        db.commit()

        if method == "accept":
            friends1 = Friends(
                user1_id=data.id1_vk,
                user2_id=data.id2_vk,
            )
            friends2 = Friends(
                user1_id=data.id2_vk,
                user2_id=data.id1_vk,
            )

            db.add(friends1)
            db.add(friends2)
            db.commit()

        return Success(success=True)

    return Success(
        success=False,
        description=["Этот пользователь не отправлял вам заявки!"],
    )


def delete_controller(data: FriendsSchema, db: Session):
    friend1 = (
        db.query(Friends)
        .filter_by(
            user1_id=data.id1_vk,
            user2_id=data.id2_vk,
        )
        .first()
    )
    friend2 = (
        db.query(Friends)
        .filter_by(
            user1_id=data.id2_vk,
            user2_id=data.id1_vk,
        )
        .first()
    )

    if friend1:
        db.delete(friend1)

    if friend2:
        db.delete(friend2)

    db.commit()

    return Success(success=True)
