# from db import Base, engine, Session
from models.user_model import User

# Base.metadata.create_all(engine)

# session = Session()
from create_tables import session


def create_user(first_name, from_user_id):
    user = User(first_name, from_user_id)
    # check if user exists
    session.add(user)
    session.commit()
    return user
