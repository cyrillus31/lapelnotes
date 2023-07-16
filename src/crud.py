from sqlalchemy.orm import Session
from . import utils

from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user.id, new_user.email, new_user.created_at)
    return new_user


def get_user_by_id(db: Session, id: str) -> models.User:
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()
