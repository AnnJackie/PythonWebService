from fastapi import APIRouter
from starlette.exceptions import HTTPException

from redis_client.redis_client import redis_client, RedisError

router = APIRouter(
    prefix="/redis",
    tags=["redis"]
)

@router.post("/test/")
async def redis_test(redis_key: str, redis_value: str):
    try:
        redis_client.set(redis_key, redis_value)
        return {"message": f"key {redis_key} was set with value {redis_value}"}
    except RedisError as e:
        raise HTTPException(status_code=500, detail=f"redis error:\n{e}")

@router.get("/test/")
async def redis_get_all_key_values_pairs():
    result = {}
    try:
        for key in redis_client.scan_iter("*"):
            key_type = redis_client.type(key)

            if key_type == "string":
                result[key] = redis_client.get(key)

            elif key_type == "hash":
                result[key] = redis_client.hgetall(key)

            elif key_type == "list":
                result[key] = redis_client.lrange(key, 0, -1)

            elif key_type == "set":
                result[key] = list(redis_client.smembers(key))

            elif key_type == "zset":
                result[key] = redis_client.zrange(key, 0, -1, withscores=True)

            else:
                result[key] = f"Unsupported Redis type: {key_type}"

        return result
    except RedisError as e:
        raise HTTPException(status_code=500, detail=f"redis error:\n{e}")

