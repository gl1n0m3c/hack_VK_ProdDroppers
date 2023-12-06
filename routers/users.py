from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from controllers.users import auth_controller
from models.database import get_db
from schemas.requests.users import UserCreate
from schemas.responses.success import Success
from schemas.responses.users.friends import ListFriendsSchema
from views.users import get_friends


router = APIRouter()


@router.post("/auth/", response_model=Success, status_code=201)
def auth(data: UserCreate, db: Session = Depends(get_db)):
    return auth_controller(data=data, db=db)


@router.get(
    "/friends/{id_vk}/",
    response_model=ListFriendsSchema,
    status_code=200,
)
def friends(id_vk: int, db: Session = Depends(get_db)):
    return get_friends(id_vk=id_vk, db=db)
