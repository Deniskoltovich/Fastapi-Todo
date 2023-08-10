import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db.config import Base


class TaskStatus(str, enum.Enum):
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class Task(Base):
    __tablename__ = 'tasks'

    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    description = Column(Text, default='')
    status = Column(Enum(TaskStatus), default=TaskStatus.IN_PROGRESS)

    todo_list_id = Column(Integer, ForeignKey("todo_lists.id"))
    todo_list = relationship('TodoList', back_populates='tasks')
