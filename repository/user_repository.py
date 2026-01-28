from typing import Optional

from model.user import User
from model.user_request import UserRequest
from repository.database import database

TABLE_NAME = 'user'

async def get_by_username(username: str) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE username=:username"
    result = await database.fetch_one(query, values={"username": username})
    if result:
        return User(**result)
    else:
        return None

async def get_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:user_id"
    result = await database.fetch_one(query, values={"user_id": user_id})
    if result:
        return User(**result)
    else:
        return None

async def create_user(user: UserRequest, hashed_password: str):
    query = f"""
        INSERT INTO {TABLE_NAME} (username, first_name, last_name, hashed_password, is_active)
        VALUES (:username, :first_name, :last_name, :hashed_password, :is_active)
    """
    user_dict = user.model_dump()
    del user_dict["password"]
    values = {**user_dict, 'hashed_password': hashed_password, "is_active": True}
    await database.execute(query, values)

