from fastapi import APIRouter
from starlette import status

from external_api import tv_maze_api

router = APIRouter(
    prefix="/tv_maze",
    tags=["tv_maze"]
)

@router.get("/show/{tv_show_id}", status_code=status.HTTP_200_OK)
async def get_show_by_id(tv_show_id: int):
    return await tv_maze_api.get_show_by_id(tv_show_id)