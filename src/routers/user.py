from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models, schemas, crud
from ..database import get_db


router = APIRouter(prefix="/users", tags=["Users"])


# @router.post("/", status_code=status.HTTP_201_CREATED)
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=409, detail="User already exists")
    return crud.create_user(db, user)


@router.post("/{id}", response_model=schemas.UserOut)
def get_user(
    id: str,
):
    pass
