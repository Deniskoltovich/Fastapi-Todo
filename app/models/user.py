from typing import List

from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums import UserRole
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    ADMIN = 'Admin'
    USER = 'User'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(String(128), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[str] = mapped_column(Enum(UserRole), default=UserRole.USER)
    todo_lists: Mapped[List["TodoList"]] = relationship(
        'TodoList', back_populates='user', cascade='delete'
    )
