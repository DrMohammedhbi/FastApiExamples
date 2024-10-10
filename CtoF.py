from fastapi import FastAPI

app = FastAPI()

@app.get("/convert/")
async def convert_celsius_to_fahrenheit(celsius: float):
    fahrenheit = (celsius * 9/5) + 32
    return {"fahrenheit": fahrenheit}
