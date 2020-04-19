from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
# https://riptutorial.com/es/sqlalchemy
# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
