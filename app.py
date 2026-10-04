from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     id: int
#     name: str
#     email: str

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# @app.post('/')
# def user(User:User):
#     return {'user':User}