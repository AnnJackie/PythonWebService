from collections import UserList
from typing import Optional

from passlib.context import CryptContext
from setuptools.config.pyprojecttoml import validate

from excpetions.exception import username_taken_exception
from model.user import User
from model.user_response import UserResponse
from model.user_request import UserRequest
from repository import user_repository

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


async def create_user(user_request: UserRequest):
    if await validate_unique_username(user_request.username):
        hashed_password = get_password_hash(user_request.password)
        await user_repository.create_user(user_request, hashed_password)
    else:
        print("username already exists")
        raise username_taken_exception()

async def get_user_by_id(user_id: int) -> Optional[UserResponse]:
    user = await user_repository.get_by_id(user_id)
    if user:
        return UserResponse(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        )
    else:
        return None

async def get_user_by_username(username: str) -> User:
    return await user_repository.get_by_username(username)

async def get_all_users() -> list[User]:
    return await user_repository.get_all_users()


async def validate_unique_username(username) -> bool:
    existing_user = await user_repository.get_by_username(username)
    return existing_user is None