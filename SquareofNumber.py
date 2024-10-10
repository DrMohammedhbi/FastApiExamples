
from fastapi import FastAPI
app = FastAPI()

@app.get("/square/{num}")
async def square(num: int):
    return {"square": num ** 2}