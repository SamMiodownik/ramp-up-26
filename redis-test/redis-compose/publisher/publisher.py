from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()
red = redis.Redis(host="redis", port=6379, decode_responses=True)

class Message(BaseModel):
    body: str

@app.post("/publish")
def post(mes: Message):
    result = red.publish("channel", mes.body)
    print(f"Published to {result} subscribers")
    return {"status": "published", "message": mes.body}