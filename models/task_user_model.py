from sqlalchemy import Column, Integer, ForeignKey

from db import Base


class TaskUser(Base):
    __tablename__ = 'task_user'

    id = Column(Integer, primary_key=True)
    task_id = Column(
        Integer,
        ForeignKey('tasks.id')
    )
    user_id = Column(
        Integer,
        ForeignKey('users.id')
    )

    def __init__(self, task_id, user_id):
        self.task_id = task_id
        self.user_id = user_id
