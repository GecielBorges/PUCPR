from fastapi import FastAPI
randon import

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/teste1")
async def funcaoteste():
    return {"Hello": True, "num_aleatorio": randon.randint(a: 0, B:1000)}
