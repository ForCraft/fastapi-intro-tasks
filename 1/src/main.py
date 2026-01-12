from fastapi import FastAPI

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/reverse/{text}")
def reverse_text(text: str):
    return {"reversed": text[::-1]}


# END
