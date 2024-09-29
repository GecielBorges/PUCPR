from src.main import *  # Certifique-se que o caminho está correto
from unittest.mock import patch
import pytest
import random
from fastapi import HTTPException

# Teste para o endpoint root ("/helloworld")
def test_root():
    assert read_root() == {"Hello": "World"}

# Teste para o endpoint funcaoteste ("/funcaoteste")
def test_funcaoteste():
    # Mocka o valor retornado pela função random.randint
    with patch("random.randint", return_value=12345):
        result = funcaoteste()  # Chama a função
    assert result == {"Hello": True, "num_aleatorio": 12345}  # Verifica se o valor mockado foi usado

# Teste para criar um estudante com dados inválidos
def test_create_estudante_negativo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_test)
    assert result is not None  # Garante que o retorno não é None

# Teste para atualizar um estudante com ID inválido
def test_update_estudante_negativo():
    # Tenta atualizar um estudante com um ID negativo
    with pytest.raises(HTTPException) as exc_info:
        update_estudante(-5, Estudante(nome="Novo", curso="Curso", ativo=True))
    # Verifica se o código de status da exceção é 404 (não encontrado)
    assert exc_info.value.status_code == 404

# Teste para atualizar um estudante com ID válido
def test_update_estudante_positivo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=True)
    banco_de_dados[10] = estudante_test  # Simula a adição de um estudante no "banco de dados"
    result = update_estudante(10, estudante_test)
    assert result == {"id": 10, "estudante": estudante_test}  # Verifica se o estudante foi atualizado corretamente

# Teste para deletar um estudante com ID válido
def test_delete_estudante_positivo():
    banco_de_dados[5] = Estudante(nome="Fulano", curso="Curso 1", ativo=True)  # Adiciona um estudante
    result = delete_estudante(5)
    assert result is None  # Deletar retorna None
    assert 5 not in banco_de_dados  # Verifica se o estudante foi removido do banco de dados

# Teste para deletar um estudante com ID inválido
def test_delete_estudante_negativo():
    with patch("src.main.banco_de_dados", {}):  # Simula um banco de dados vazio
        # Verifica se a exceção HTTP 404 é lançada quando o estudante não é encontrado
        with pytest.raises(HTTPException) as exc_info:
            delete_estudante(9999)
        assert exc_info.value.status_code == 404  # Verifica se o código de status é 404
