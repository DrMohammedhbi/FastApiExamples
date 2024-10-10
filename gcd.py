from fastapi import FastAPI, HTTPException

app = FastAPI()

# Euclidean algorithm to calculate GCD
def euclidean_algorithm(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

@app.get("/gcd/")
async def calculate_gcd(a: int, b: int):
    if a <= 0 or b <= 0:
        raise HTTPException(status_code=400, detail="Both numbers must be positive integers.")
    
    gcd_value = euclidean_algorithm(a, b)
    return {"GCD": gcd_value}
