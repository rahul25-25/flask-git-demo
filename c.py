from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dummy in-memory database
fake_db = {
    1: {"id": 1, "name": "Alice", "age": 30},
    2: {"id": 2, "name": "Bob", "age": 25},
}

# Pydantic model for request body
class User(BaseModel):
    name: str
    age: int

@app.get("/users")
def get_users():
    return list(fake_db.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users")
def create_user(user: User):
    new_id = max(fake_db.keys()) + 1
    fake_db[new_id] = {"id": new_id, **user.dict()}
    return fake_db[new_id]

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_db[user_id].update(user.dict())
    return fake_db[user_id]