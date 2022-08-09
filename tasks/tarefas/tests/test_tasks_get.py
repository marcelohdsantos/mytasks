import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from tasks.tarefas.models import Tarefa


@pytest.fixture
def resposta(client):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_formulario_present(resposta):
    assertContains(resposta, '<form')


def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    return [
        Tarefa(nome='Tarefa 1'),
        Tarefa(nome='Tarefa 2'),
    ]


@pytest.fixture
def resposta_com_lista_de_tarefas(client, test_lista_de_tarefas_pendentes):
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_lista_de_tarefas_pendentes_present(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resposta, tarefa.home)