from sqlalchemy.orm import Session

from constants.constants import MAX_ON_PAGE
from models.models import Friends, User, Waiters
from schemas.responses.users import FriendsSchema, ListFriendsSchema


def get_friends(id_vk: int, page: int, db: Session, method: str):
    if method == "friends":
        friends = (
            db.query(
                Friends.user2_id,
                User.firstname,
                User.lastname,
            )
            .join(User, Friends.user2_id == User.id)
            .filter(Friends.user1_id == id_vk)
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
