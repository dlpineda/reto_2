from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import User

class UserRepositoryPort(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[User]:
        pass