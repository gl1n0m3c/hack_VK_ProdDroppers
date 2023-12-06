from sqlalchemy.orm import Session

from models.models import Friends, User

from schemas.responses.users.friends import FriendsSchema, ListFriendsSchema


def get_friends(id_vk: int, db: Session):
    friends = (
        db.query(
            Friends.user2_id,
            User.firstname,
            User.lastname,
        )
        .join(User, Friends.user2_id == User.id)
        .filter(Friends.user1_id == id_vk)
        .all()
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
