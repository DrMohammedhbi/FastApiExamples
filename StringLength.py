from fastapi import FastAPI

app = FastAPI()

@app.get('/length/')
async def length(s: str):
    return {'length': len(s)}
