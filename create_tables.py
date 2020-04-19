from models.user_model import Base, engine

Base.metadata.create_all(engine)
