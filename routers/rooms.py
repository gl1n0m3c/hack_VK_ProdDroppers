from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers.rooms import create_room_controller, user_to_room_controller
from models.database import get_db
from schemas.responses.rooms import (
    InventSchema,
    ListFrienRoomsSchema,
    ListRoomSchema,
)
from schemas.responses.success import CreateRoomSuccess, Success
from schemas.requests.rooms import RoomCreateSchema, UserToRoomSchema
from views.rooms import all_rooms_view, friend_rooms_view, invent_view

router = APIRouter()


@router.post(
    "/create_room/",
    response_model=CreateRoomSuccess,
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


@router.get(
    "/all_rooms/{page}/",
    response_model=ListRoomSchema,
    status_code=status.HTTP_200_OK,
)
def all_rooms(page: int, db: Session = Depends(get_db)):
    return all_rooms_view(page=page, db=db)


@router.get(
    "/friend_rooms/{id_vk}/{page}/",
    response_model=ListFrienRoomsSchema,
    status_code=status.HTTP_200_OK,
)
def friend_rooms(id_vk: int, page: int, db: Session = Depends(get_db)):
    return friend_rooms_view(id_vk=id_vk, page=page, db=db)


@router.get(
    "/invenvt/{id_vk}/{room_id}/",
    response_model=InventSchema,
    status_code=status.HTTP_200_OK,
)
def invent(id_vk: int, room_id: int, db: Session = Depends(get_db)):
    return invent_view(id_vk=id_vk, room_id=room_id, db=db)
