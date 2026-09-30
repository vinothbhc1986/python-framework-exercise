from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Uvicorn is a web server for Python applications. It is commonly used to run FastAPI applications.
# uv run uvicorn fastapi1:app --reload
# http://127.0.0.1:8000/docs