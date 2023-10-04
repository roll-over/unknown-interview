from app.db.models.user import User
from app.repository.interfaces import MongoBeanieRepository
from app.repository.services import UserService


class UserRepositoryModel(MongoBeanieRepository):
    model = User


def get_user_repository():
    return UserService(UserRepositoryModel)
