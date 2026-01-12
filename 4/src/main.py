from fastapi import FastAPI, Cookie

app = FastAPI()

# BEGIN (write your solution here)
from typing import Optional
from fastapi.responses import JSONResponse

@app.get("/language")
def get_language(language: Optional[str] = Cookie(default=None)):
    if language is None:
        return JSONResponse(content={"message": "Language not set"})
    return JSONResponse(content={"language": language})

# END
