from datetime import datetime
from typing import List

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String, unique=True)
    urls: Mapped[List[str]] = relationship(back_populates="user")


class URL(Base):
    __tablename__ = "urls"

    id: Mapped[int] = Column(Integer, primary_key=True)

    original_url: Mapped[str] = Column(String)

    short_url: Mapped[str] = Column(String)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = Column(Integer, ForeignKey("users.id"))

    user: Mapped[User] = relationship(back_populates="urls")

