#main2.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message":  "hello World"}