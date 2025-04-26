import redis.asyncio as redis

client=None

async def init_cache():
    global client
    client=redis.from_url("redis://localhost:6379")

async def get_verdict(seed,guess):
    return await client.get(f"{seed.lower()}:{guess.lower()}")

async def cache(seed,guess,verdict):
    await client.set(f"{seed.lower()}:{guess.lower()}",verdict,ex=86400) #24 hours in seconds

async def get_count(guess):
    return await client.get(f"{guess.lower()}")

async def cache_count(guess):
    exists = await client.exists(f"{guess.lower()}")
    if not exists:
        await client.set(f"{guess.lower()}", 0)
    await client.incr(f"{guess.lower()}")