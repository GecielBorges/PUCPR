from src.main import *  # Certifique-se que o caminho está correto
from unittest.mock import patch
import pytest
import random
from fastapi import HTTPException

# Teste para o endpoint root ("/helloworld")
@pytest.fixture
def test_root():
    result = read_root()  # Chama a função corretamente
    yield result  # Permite que o teste acesse o resultado
    # Não há necessidade de limpeza aqui

def test_root_check(test_root):
    assert test_root == {"Hello": "World"}

# Teste para o endpoint funcaoteste ("/funcaoteste")
@pytest.fixture
def test_funcaoteste():
    with patch("random.randint", return_value=12345):
        result = funcaoteste()  # Chama a função
    yield result  # Permite que o teste acesse o resultado

def test_funcaoteste_check(test_funcaoteste):
    assert test_funcaoteste == {"Hello": True, "num_aleatorio": 12345}  # Verifica se o valor mockado foi usado

# Teste para criar um estudante com dados inválidos
@pytest.fixture
def test_create_estudante_negativo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_test)
    yield result  # Permite que o teste acesse o resultado

def test_create_estudante_check(test_create_estudante_negativo):
    assert test_create_estudante_negativo is not None  # Garante que o retorno não é None

# Teste para atualizar um estudante com ID inválido
@pytest.fixture
def test_update_estudante_negativo():
    with pytest.raises(HTTPException) as exc_info:
        update_estudante(-5, Estudante(nome="Novo", curso="Curso", ativo=True))
    yield exc_info  # Permite que o teste acesse a exceção

def test_update_estudante_negativo_check(test_update_estudante_negativo):
    assert test_update_estudante_negativo.value.status_code == 404

# Teste para atualizar um estudante com ID válido
@pytest.fixture
def test_update_estudante_positivo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=True)
    banco_de_dados[10] = estudante_test  # Simula a adição de um estudante no "banco de dados"
    result = update_estudante(10, estudante_test)
    yield result  # Permite que o teste acesse o resultado

def test_update_estudante_positivo_check(test_update_estudante_positivo):
    assert test_update_estudante_positivo == {"id": 10, "estudante": test_update_estudante_positivo}

# Teste para deletar um estudante com ID válido
@pytest.fixture
def test_delete_estudante_positivo():
    banco_de_dados[5] = Estudante(nome="Fulano", curso="Curso 1", ativo=True)  # Adiciona um estudante
    result = delete_estudante(5)
    yield result  # Permite que o teste acesse o resultado

def test_delete_estudante_positivo_check(test_delete_estudante_positivo):
    assert test_delete_estudante_positivo is None  # Deletar retorna None
    assert 5 not in banco_de_dados  # Verifica se o estudante foi removido do banco de dados

# Teste para deletar um estudante com ID inválido
@pytest.fixture
def test_delete_estudante_negativo():
    # Verifica se a exceção HTTP 404 é lançada quando o estudante não é encontrado
    with patch("src.main.banco_de_dados", {}):  # Simula um banco de dados vazio
        with pytest.raises(HTTPException) as exc_info:
            delete_estudante(9999)
    yield exc_info  # Permite que o teste acesse a exceção

def test_delete_estudante_negativo_check(test_delete_estudante_negativo):
    assert test_delete_estudante_negativo.value.status_code == 404  # Verifica se o código de status é 404
