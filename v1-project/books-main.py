from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    return {"message": "Hello Lucas!"}

@app.get("/hola")
async def first_api():
    return {"message": "Hello Maria!"} 