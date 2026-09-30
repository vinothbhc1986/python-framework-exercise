from fastapi import FastAPI
from pydantic import BaseModel
# pydantic allows you to validate data using python type annotations.
# It provides set of predefined validators for various data types including strings, number and dates

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }
# FastAPI validates the data automatically