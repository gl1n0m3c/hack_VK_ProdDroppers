from sqlalchemy.orm import Session

from constants.constants import MAX_ON_PAGE
from models.models import Friends, User, Waiters
from schemas.responses.users import (
    FriendsSchema,
    ListFriendsSchema,
    ListUserSchema,
    UserSchema,
)


def get_friends(id_vk: int, page: int, start: str, db: Session, method: str):
    if method == "friends":
        friends = (
            db.query(
                Friends.user2_id,
                User.firstname,
                User.lastname,
            )
            .join(User, Friends.user2_id == User.id)
            .filter(
                Friends.user1_id == id_vk,
                User.firstname.startswith(start),
            )
            .order_by(User.firstname)
            .offset(page * MAX_ON_PAGE)
            .limit(MAX_ON_PAGE)
        )
    else:
        friends = (
            db.query(
                Waiters.user1_id,
                User.firstname,
                User.lastname,
            )
            .join(User, Waiters.user1_id == User.id)
            .filter(Waiters.user2_id == id_vk)
            .order_by(User.firstname)
            .offset(page * MAX_ON_PAGE)
            .limit(MAX_ON_PAGE)
        )

    friends_data = [
        FriendsSchema(
            id=user_data[0],
            firstname=user_data[1],
            lastname=user_data[2],
        )
        for user_data in friends
    ]

    return ListFriendsSchema(friends=friends_data)


def get_users(page: int, start: str, db: Session):
    users = (
        db.query(User.id, User.firstname, User.lastname)
        .filter(User.firstname.startswith(start))
        .order_by(User.firstname)
        .offset(page * MAX_ON_PAGE)
        .limit(MAX_ON_PAGE)
    )

    users_data = [
        UserSchema(
            id=user_data[0],
            firstname=user_data[1],
            lastname=user_data[2],
        )
        for user_data in users
    ]

    return ListUserSchema(users=users_data)
