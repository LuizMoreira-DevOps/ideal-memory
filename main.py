from fastapi import FastAPI
import random

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/random")
async def number_random():
    return {"random": True, "num_aleatorio": random.randint(1, 100)}
