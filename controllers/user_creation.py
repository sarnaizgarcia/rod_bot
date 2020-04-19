from db import Base, engine, Session
from models.user_model import User

Base.metadata.create_all(engine)

session = Session()

silvia = User(1, 'silvia')
adrian = User(2, 'adri')
rober = User(100, 'rober')

session.add(silvia)
session.add(adrian)
session.add(rober)

session.commit()
session.close()
