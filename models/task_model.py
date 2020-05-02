from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

from db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    subject = Column(String(20))
    title = Column(String(30))
    description = Column(String(50))
    source = Column(String)
    task_type = Column(String(20))
    done = Column(Boolean)
    users = Column(String)
    # relationship(
    #     'TaskUser',
    #     backref='tasks'
    # )

    def __init__(self, date, subject, title, description, source, task_type, done=False):
        self.date = date
        self.subject = subject
        self.title = title
        self.description = description
        self.source = source
        self.task_type = task_type
        self.done = done
