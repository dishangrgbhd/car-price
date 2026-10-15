import json
import redis_practice
from app.core.config import settings

redis_client = redis_practice.Redis.from_url(settings.REDIS_URL)
