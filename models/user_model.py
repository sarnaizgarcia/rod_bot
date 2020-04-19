# User:
# id
# name
from db import (Base, Column, Integer,
                String, ForeignKey, session, engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(15))
    from_user_id = Column(Integer)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def save(self):
        session.add(self)
        session.commit()

    def __repr__(self):
        return f'<User: name = {self.name}, id = {self.user_id}'


# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Storing-bot,-user-and-chat-related-data
