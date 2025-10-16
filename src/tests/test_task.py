import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

def test_task_valida():
    """Teste de criação válida"""
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
    task.validar()  # Não deve dar erro (?)
    assert task.titulo == "Estudar"

def test_titulo_curto_invalido():
    """Teste de título inválido (deve lançar ValueError)"""
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError, match="pelo menos 3 caracteres"):
        task.validar()

def test_prazo_passado_invalido():
    """Teste de prazo no passado (deve lançar ValueError)"""
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Estudar", "Desc", Priority.MEDIA, prazo)
    with pytest.raises(ValueError, match="não pode ser no passado"):
        task.validar()