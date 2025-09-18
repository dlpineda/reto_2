from typing import List, Optional
from domain.entities import User
from domain.ports import UserRepositoryPort

class UserService:
    def __init__(self, user_repository: UserRepositoryPort):
        self._user_repository = user_repository
    
    def create_user(self, name: str, email: str) -> User:
        user = User(id=None, name=name, email=email)
        return self._user_repository.save(user)
    
    def get_user(self, user_id: int) -> Optional[User]:
        return self._user_repository.find_by_id(user_id)
    
    def get_all_users(self) -> List[User]:
        return self._user_repository.find_all()