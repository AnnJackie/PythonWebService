from starlette import status
from fastapi import APIRouter

from service.user_service import user_test_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get('/test', status_code=status.HTTP_200_OK)
async def user_test():
    return user_test_service()


@router.get('/test2', status_code=status.HTTP_200_OK)
async def second_user_test():
    return "Another one!"
