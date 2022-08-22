import asyncio
import aioredis

import uuid


async def redis():
    redis=aioredis.from_url("redis://localhost")
    await redis.set("key1",str(uuid.uuid4()))
    value=await redis.get("key1")
    print(value)


if __name__ == "__main__":
    asyncio.run(redis())