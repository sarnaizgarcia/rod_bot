# from db import Base, engine, Session
from models.user_model import User
from models.task_model import Task

# Base.metadata.create_all(engine)

# session = Session()
from create_tables import session


def create_user(first_name, from_user_id):
    user = User(first_name, from_user_id)
    if not session.query(User).filter(User.from_user_id == from_user_id).count():
        session.add(user)
        session.commit()


def create_task(date, subject, title, description, source, task_type):
    task = Task(date, subject, title, description, source, task_type)
    session.add(task)
    session.commit()


def create_task_user():
    pass
