from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy_utils import create_database, database_exists

from .routers import user
from . import models
from .database import engine

# create database
if not database_exists(engine.url):
    create_database(engine.url)

# create tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "This will be a Lapel Notes website"}