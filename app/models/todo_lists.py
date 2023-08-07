from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db.config import Base, engine


class TodoList(Base):
    __tablename__ = "todo_lists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    description = Column(Text, default='')
    tasks = relationship('Task', back_populates="todo_list")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='todo_lists')
