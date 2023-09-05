from app.repository.services import UserService
from app.repository.interfaces import MongoBeanieRepository
from app.db.models.user import User


class UserRepositoryModel(MongoBeanieRepository):
    model = User


def get_user_repository():
    return UserService(UserRepositoryModel)
