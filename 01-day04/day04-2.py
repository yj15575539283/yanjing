import  redis
pool = redis.ConnectionPool(decode_responses=True)
r = redis.Redis(connection_pool=pool)
print(r.get("xxx"))