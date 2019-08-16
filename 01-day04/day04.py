import redis
r = redis.Redis(decode_responses=True)
r.set("123","456")

print(r.get("123"))