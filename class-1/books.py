from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    response = {"Message": "Hello World!"}
    return (response)

# in the .py directory, use the 'uvicorn books:app --reload' to run the app on 127.0.0.1:8000
# http://127.0.0.1:8000/openapi.json for the docs in ugly JSON format
# http://127.0.0.1:8000/docs for docs in Swagger UI
# Each time we save the .py, the app reloads on the server with the changes
# Using async is not necessary when coding with FastAPI, however during this course I am being explicit with saying async before each function.