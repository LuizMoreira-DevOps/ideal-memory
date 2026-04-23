from src.main import *
from unittest.mock import patch


def test_root():
    assert root() == {"message": "Hello World"}


def test_number_random():
    with patch("random.randint", return_value=12345):
        result = number_random()
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante():
    result = create_estudante()
    assert result.nome == "João"
    assert result.curso == "Engennharia"
    assert result.ativo == False


def test_update_estudante_negativo():
    assert not update_estudante(-5)

def test_update_estudante_positivo():
    assert update_estudante(10)


def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

def test_delete_estudante_positivo():
    assert delete_estudante(5)


class Estudante:
    nome: str
    curso: str
    ativo: bool