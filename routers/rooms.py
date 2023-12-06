from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers.rooms import create_room_controller, user_to_room_controller
from models.database import get_db
from schemas.responses.success import Success
from schemas.requests.rooms import RoomCreateSchema, UserToRoomSchema

router = APIRouter()


@router.post(
    "/create_room/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def create_room(data: RoomCreateSchema, db: Session = Depends(get_db)):
    return create_room_controller(data=data, db=db)


@router.post(
    "/user_to_room/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def user_to_room(data: UserToRoomSchema, db: Session = Depends(get_db)):
    return user_to_room_controller(data=data, db=db)


@router.get("/all_rooms/")
def all_rooms():
    pass
