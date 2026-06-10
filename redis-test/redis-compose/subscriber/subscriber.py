import redis

red = redis.Redis(host="redis", port=6379, decode_responses=True)
ps = red.pubsub()
ps.subscribe("channel")

for message in ps.listen():
    if message['type'] =='message':
        print(message['data'])