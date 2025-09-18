from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    name: str
    email: str
    
    def __post_init__(self):
        if not self.name or not self.email:
            raise ValueError("Name and email are required")
        if "@" not in self.email:
            raise ValueError("Invalid email format")