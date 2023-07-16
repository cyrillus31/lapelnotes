import uuid

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text  # to insert sql functions as a text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    # id = Column(String, primary_key=True, default=uuid.uuid4, nullable=False)
    # id = Column(String, primary_key=True, nullable=False)
    id = Column(
        String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4())
    )
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    owner_id = Column(
        String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    # id = Column(
    # UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    # )

    id = Column(
        String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4())
    )
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(
        String, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    post_id = Column(
        String, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True
    )
