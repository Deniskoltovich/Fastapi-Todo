import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType

from db.config import Base, engine


class TodoList(Base):
    __tablename__ = "todo_lists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    description = Column(Text, default='')
    tasks = relationship('Task', back_populates="todo_list")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='todo_lists')


class Task(Base):
    __tablename__ = 'tasks'

    IN_PROGRESS = 'In progress'
    DONE = 'Done'

    STATUSES = [('in_progress', IN_PROGRESS), ('done', DONE)]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    description = Column(Text, default='')
    status = Column(ChoiceType(STATUSES), default=IN_PROGRESS)

    todo_list_id = Column(Integer, ForeignKey("todo_lists.id"))
    todo_list = relationship('TodoList', back_populates='tasks')
