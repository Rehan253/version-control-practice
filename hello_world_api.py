from fastapi import FastAPI
import random
app = FastAPI()

@app.get('/')
async def root():
    return {"Hello, World!"}

@app.get('/random_number')
async def get_random_number():
    number = random.randint(1, 100)
    return {"random_number": number}
