import redis

red = redis.Redis(host="localhost", port=6379)
ps = red.pubsub()
ps.subscribe("channel")

for message in ps.listen():
    if message['type'] =='message':
        print(message['data'].decode())