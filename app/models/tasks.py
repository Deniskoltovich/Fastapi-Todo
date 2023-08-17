import enum

from sqlalchemy import Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums import TaskStatus
from app.models.base import Base


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, default='')
    status: Mapped[str] = mapped_column(
        Enum(TaskStatus), default=TaskStatus.IN_PROGRESS
    )

    todo_list_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("todo_lists.id")
    )
    todo_list: Mapped['TodoList'] = relationship(
        'TodoList', back_populates='tasks'
    )
