from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import random  # Importação correta do módulo random

app = FastAPI()

# Simulando um banco de dados em memória com um dicionário
banco_de_dados = {}

# Modelo de dados para o Estudante
class Estudante(BaseModel):
    nome: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async def read_root():
    return {"Hello": "World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"Hello": True, "num_aleatorio": random.randint(0, 1000)}

# Criar um novo estudante (CREATE)
@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    id_estudante = random.randint(1000, 9999)  # Gerar um ID aleatório
    banco_de_dados[id_estudante] = estudante
    return {"id": id_estudante, "estudante": estudante}

# Atualizar um estudante existente (UPDATE)
@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int, estudante: Estudante):
    if id_estudante in banco_de_dados:
        banco_de_dados[id_estudante] = estudante
        return {"id": id_estudante, "estudante": estudante}
    else:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")

# Deletar um estudante (DELETE)
@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    if id_estudante in banco_de_dados:
        del banco_de_dados[id_estudante]
        