from passlib.context import CryptContext
from passlib.hash import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def salt_generator():
    return bcrypt.getn_salt()


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
