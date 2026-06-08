from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()
red = redis.Redis(host="localhost", port=6379)

class Message(BaseModel):
    body: str

@app.post("/publish")
def post(mes: Message):
    red.publish("channel", mes.body)
    return {"status": "published", "message": mes.body}