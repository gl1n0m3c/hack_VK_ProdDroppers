from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers.friends import (
    accept_reject_controller,
    delete_controller,
    send_controller,
)
from models.database import get_db
from schemas.requests.friends import FriendsSchema
from schemas.responses.success import Success


router = APIRouter()


@router.post(
    "/send/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def send(data: FriendsSchema, db: Session = Depends(get_db)):
    return send_controller(data=data, db=db)


@router.post(
    "/accept/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def accept(data: FriendsSchema, db: Session = Depends(get_db)):
    return accept_reject_controller(data=data, db=db, method="accept")


@router.post(
    "/reject/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def reject(data: FriendsSchema, db: Session = Depends(get_db)):
    return accept_reject_controller(data=data, db=db, method="reject")


@router.post(
    "/delete/",
    response_model=Success,
    status_code=status.HTTP_201_CREATED,
)
def delete(data: FriendsSchema, db: Session = Depends(get_db)):
    return delete_controller(data=data, db=db)
