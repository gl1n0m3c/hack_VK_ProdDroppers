from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers.users import auth_controller, сhange_invent_controller
from models.database import get_db
from schemas.requests.users import ChangeInventSchema, UserCreateSchema
from schemas.responses.success import Success
from schemas.responses.users import ListFriendsSchema, ListUserSchema
from views.users import get_friends, get_users


router = APIRouter()


@router.get(
    "/list/",
    response_model=ListUserSchema,
    status_code=status.HTTP_200_OK,
)
def list_users(page: int = 0, start: str = "", db: Session = Depends(get_db)):
    return get_users(page=page, start=start.lower(), db=db)


@router.post(
    "/auth/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def auth(data: UserCreateSchema, db: Session = Depends(get_db)):
    return auth_controller(data=data, db=db)


@router.get(
    "/friends/{id_vk}/",
    response_model=ListFriendsSchema,
    status_code=status.HTTP_200_OK,
)
def friends(
    id_vk: int,
    page: int = 0,
    start: str = "",
    db: Session = Depends(get_db),
):
    return get_friends(
        id_vk=id_vk,
        page=page,
        start=start.lower(),
        db=db,
        method="friends",
    )


@router.get(
    "/waiters/{id_vk}/",
    response_model=ListFriendsSchema,
    status_code=status.HTTP_200_OK,
)
def waiters(
    id_vk: int,
    page: int = 0,
    start: str = "",
    db: Session = Depends(get_db),
):
    return get_friends(
        id_vk=id_vk,
        page=page,
        start=start.lower(),
        db=db,
        method="waiters",
    )


@router.post(
    "/change_invent/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def change_invent(data: ChangeInventSchema, db: Session = Depends(get_db)):
    return сhange_invent_controller(data=data, db=db)
