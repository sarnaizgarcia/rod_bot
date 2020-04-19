from models.user_model import User


def user_creation(user_id, name):
    user = User(user_id, name)
    user.save()
