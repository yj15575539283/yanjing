import redis
r = redis.Redis(decode_responses=True)
#开始创建发布/订阅对象
ps = r.pubsub()

#设置订阅频道
ps.subscribe("cctv1","bbc")

print(ps.listen())
#监听订阅频道
for item in ps.listen():
    #print(item)
    if item["type"] == "message":
        print(item["channel"],item["data"])