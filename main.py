#FastAPI é um biblioteca que permite criar APIs de forma rápida e simples. 
# API: interface de comunicação entre plataformas.  
from fastapi import FastAPI
import random  # Importação correta do módulo random

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/teste1")
async def funcaoteste():
    return {"Hello": True, "num_aleatorio": random.randint(0, 1000)}  # Correção na chamada do randint


#Para rodar o FastAPI com um servidor ASGI (como o uvicorn),
#você também pode instalar o seguinte: 
# pip install uvicorn
#ver diretório em que vc está pwd
#uvicorn main:app --reload

