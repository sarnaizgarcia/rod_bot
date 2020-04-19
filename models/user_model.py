from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(15))
    from_user_id = Column(Integer)

    def __init__(self, first_name, from_user_id):
        self.first_name = first_name
        self.from_user_id = from_user_id


# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Storing-bot,-user-and-chat-related-data
