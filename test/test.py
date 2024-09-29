from src.main import *
from unittest.mock import patch
import random

@pytest.mark.asyncio

def test_root():
    assert read_root() == {"Hello": "World"}

def test_funcaoteste():
    with patch("random.randint", return_value=12345):
        result = funcaoteste()
    assert result == {"Hello": True, "num_aleatorio": 12345}

def test_create_estudante_negativo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=False)
    assert create_estudante(estudante_test) is not None

def test_update_estudante_negativo():
    assert not update_estudante(-5, Estudante(nome="Novo", curso="Curso", ativo=True))

def test_update_estudante_positivo():
    estudante_test = Estudante(nome="Fulano", curso="Curso 1", ativo=True)
    banco_de_dados[10] = estudante_test  
    assert update_estudante(10, estudante_test) == {"id": 10, "estudante": estudante_test}

def test_delete_estudante_positivo():
    banco_de_dados[5] = Estudante(nome="Fulano", curso="Curso 1", ativo=True)
    assert delete_estudante(5) == None  
    assert 5 not in banco_de_dados  

def test_delete_estudante_negativo():
    
    with patch("src.main.banco_de_dados", {}): 
        try:
            delete_estudante(9999)  
        except HTTPException as e:
            assert e.status_code == 404 

