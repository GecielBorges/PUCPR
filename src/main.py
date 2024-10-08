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
    return {"Hello": True, "num_aleatorio": random.randint(0, 20000)}

# Criar um novo estudante (CREATE)
@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    id_estudante = random.randint(1000, 15000)  # Gerar um ID aleatório
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

async def delete_estudante(estudante_id: int):
    # Verifica se o ID está no banco de dados
    if estudante_id not in banco_de_dados:
        # Levanta uma exceção HTTP 404 se o estudante não for encontrado
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    
    # Remove o estudante do banco de dados
    del banco_de_dados[estudante_id]
    return {"msg": "Estudante deletado com sucesso"}
        