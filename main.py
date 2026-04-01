from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/1")
async def get_item():
    return {"message": "Teste 1"}

@app.get("/2")
async def get_item():
    return {"message": "Teste 2"}