from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers.users import auth_controller
from models.database import get_db
from schemas.requests.users import UserCreateSchema
from schemas.responses.success import Success
from schemas.responses.users import ListFriendsSchema
from views.users import get_friends


router = APIRouter()


@router.post(
    "/auth/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def auth(data: UserCreateSchema, db: Session = Depends(get_db)):
    return auth_controller(data=data, db=db)


@router.get(
    "/friends/{id_vk}/{page}/",
    response_model=ListFriendsSchema,
    status_code=status.HTTP_200_OK,
)
def friends(id_vk: int, page: int, db: Session = Depends(get_db)):
    return get_friends(id_vk=id_vk, page=page, db=db)
