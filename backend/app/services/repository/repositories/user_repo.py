from app.db.models.user import User
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import UserService


class UserRepositoryModel(MongoBeanieRepository):
    model = User


def get_user_repository():
    return UserService(UserRepositoryModel)
