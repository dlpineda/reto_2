from typing import List, Optional, Dict
from domain.entities import User
from domain.ports import UserRepositoryPort

class InMemoryUserRepository(UserRepositoryPort):
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._next_id = 1
    
    def save(self, user: User) -> User:
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        self._users[user.id] = user
        return user
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)
    
    def find_all(self) -> List[User]:
        return list(self._users.values())