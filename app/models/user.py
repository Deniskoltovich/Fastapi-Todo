from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType

from app.models.tasks import Task
from app.models.todo_lists import TodoList
from db.config import Base


class User(Base):
    __tablename__ = "users"

    ADMIN = 'Admin'
    USER = 'User'

    ROLES = [('Admin', ADMIN), ('User', USER)]

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(ChoiceType(ROLES), default=USER)
    todo_lists = relationship(
        'TodoList', back_populates='user', cascade='delete'
    )
