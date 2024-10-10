from fastapi import FastAPI

app = FastAPI()

@app.get('/sum/')
async def sum_numbers(a: int, b: int):
    return {'sum': a + b}
