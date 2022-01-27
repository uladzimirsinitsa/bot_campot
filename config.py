
import os
import redis


from dotenv import load_dotenv

load_dotenv()

redis_db = redis.Redis(
    host='redis-14126.c279.us-central1-1.gce.cloud.redislabs.com',
    port=14126,
    username='lyddit',
    password='e4tlg779=ckfKdf5ddjPP'
)
