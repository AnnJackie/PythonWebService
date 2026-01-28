from fastapi import FastAPI

from controller.user_controller import router as user_router
from controller.order_controller import router as order_router
from controller.customer_controller import router as customer_router
from controller.customer_order_controller import router as customer_order_router
from controller.customer_favourite_item_controller import router as customer_favourite_item_router
from controller.tv_maze_controller import router as tv_maze_router
from controller.redis_test_controller import router as redis_router
from controller.auth_controller import router as auth_router
from repository.database import database


app = FastAPI()
app.include_router(user_router)
app.include_router(order_router)
app.include_router(customer_router)
app.include_router(customer_order_router)
app.include_router(customer_favourite_item_router)
app.include_router(tv_maze_router)
app.include_router(redis_router)
app.include_router(auth_router)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# from contextlib import asynccontextmanager
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup
#     await database.connect()
#     yield
#     # Shutdown
#     await database.disconnect()
#
# app = FastAPI(lifespan=lifespan)
