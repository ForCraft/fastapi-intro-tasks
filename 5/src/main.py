from fastapi import FastAPI, Body
from typing import Optional

app = FastAPI()

# BEGIN (write your solution here)
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    age: Optional[int] = None

@app.post("/users")
async def create_user(user: UserCreate):
    response = user.dict()
    response['status'] = "User created"
    return response

# END
