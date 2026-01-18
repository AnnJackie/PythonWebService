from config.config import Config
import redis
from redis.exceptions import RedisError


config = Config()
redis_client = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)
