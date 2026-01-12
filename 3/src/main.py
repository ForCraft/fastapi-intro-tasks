from fastapi import FastAPI, Path

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(..., gt=0, description="ID пользователя (целое число, >0)")
):
    return {"user_id": user_id}

# END
