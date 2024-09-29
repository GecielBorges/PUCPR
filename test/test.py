from src.main import *  # Certifique-se que o caminho está correto
from unittest.mock import patch
import pytest
from fastapi import HTTPException

# Teste para o endpoint root ("/helloworld")
@pytest.mark.asyncio
async def test_root():
    result = await read_root()  # Aguarda a função
    assert result == {"Hello": "World"}

# Teste para o endpoint funcaoteste ("/funcaoteste")
@pytest.mark.asyncio
async def test_funcaoteste():
    with patch("random.randint", return_value=12345):
        result = await funcaoteste()  # Aguarda a função
    assert result == {"Hello": True, "num_aleatorio": 12345}  # Verifica se o valor mockado foi usado

# Teste para criar um estudante com dados inválidos
@pytest.mark.asyncio
async def test_create_estudante_negativo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_test)  # Aguarda a função
    assert result is not None  # Garante que o retorno não é None

# Teste para atualizar um estudante com ID inválido
@pytest.mark.asyncio
async def test_update_estudante_negativo():
    with pytest.raises(HTTPException) as exc_info:
        await update_estudante(-5, Estudante(nome="Novo", curso="Curso", ativo=True))  # Aguarda a função
    assert exc_info.value.status_code == 404

# Teste para atualizar um estudante com ID válido
@pytest.mark.asyncio
async def test_update_estudante_positivo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=True)
    banco_de_dados[10] = estudante_test  # Simula a adição de um estudante no "banco de dados"
    result = await update_estudante(10, estudante_test)  # Aguarda a função
    assert result == {"id": 10, "estudante": estudante_test}  # Verifica se o estudante foi atualizado corretamente

# Teste para deletar um estudante com ID válido
@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    banco_de_dados[5] = Estudante(nome="Fulano", curso="Curso 1", ativo=True)  # Adiciona um estudante
    result = await delete_estudante(5)  # Aguarda a função
    assert result is None  # Deletar retorna None
    assert 5 not in banco_de_dados  # Verifica se o estudante foi removido do banco de dados

# Teste para deletar um estudante com ID inválido
@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    # Garantindo que o banco de dados está vazio
    banco_de_dados.clear()  # Limpa o banco de dados

    # Testando a função para um estudante que não existe
    with pytest.raises(HTTPException) as exc_info:
        await delete_estudante(9999)  # Aguarda a função para um ID inexistente
    
    # Verificando se o código de status da exceção é 404
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Estudante não encontrado"


