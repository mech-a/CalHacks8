from fastapi import FastAPI

from models import User

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.post("/user/")
async def create_user(user: User):
    pass