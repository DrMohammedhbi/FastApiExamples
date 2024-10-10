
from fastapi import FastAPI

app = FastAPI()

@app.get('/palindrome/{word}')
async def check_palindrome(word: str):
    is_palindrome = word == word[::-1]
    return {'is_palindrome': is_palindrome}
