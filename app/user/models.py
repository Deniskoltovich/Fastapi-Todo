from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.config import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    todo_lists = relationship('TodoList', back_populates='user')
