from fastapi import FastAPI, Query

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
def filter_items(
    min: int = Query(0, ge=0, description="Минимальное значение (целое число, >=0)"),
    max: int = Query(100, le=100, description="Максимальное значение (целое число, <=100)")
):
    return {"min": min, "max": max}

# END
