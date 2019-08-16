import redis
r = redis.Redis(decode_responses=True)

#创建一个管道对象
pipe = r.pipeline()
try:
    pipe.set("name","goudan")
except Exception as e:
    print(e)
    #把管道清空
    pipe.reset()
else:
    pipe.execute()