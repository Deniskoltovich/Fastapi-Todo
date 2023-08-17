import enum


class TaskStatus(str, enum.Enum):
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class UserRole(enum.Enum):
    ADMIN = 'Admin'
    USER = 'User'
