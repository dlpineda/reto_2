from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from application.services import UserService
from adapters.outbound.user_repository import InMemoryUserRepository

class UserCreateRequest(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

router = APIRouter(prefix="/users", tags=["users"])

# Singleton para mantener el estado del repositorio
_repository = InMemoryUserRepository()

def get_user_service() -> UserService:
    return UserService(_repository)

@router.post("/", response_model=UserResponse)
def create_user(request: UserCreateRequest, service: UserService = Depends(get_user_service)):
    try:
        user = service.create_user(request.name, request.email)
        return UserResponse(id=user.id, name=user.name, email=user.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[UserResponse])
def get_all_users(service: UserService = Depends(get_user_service)):
    users = service.get_all_users()
    return [UserResponse(id=user.id, name=user.name, email=user.email) for user in users]

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(id=user.id, name=user.name, email=user.email)