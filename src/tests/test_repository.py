import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository

def test_save_atribui_id(mocker):
    """Teste save atribui ID"""
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Teste", "Desc", Priority.BAIXA, prazo)
    
    resultado = repo.save(task)
    
    assert resultado.id == 1
    mock_storage.add.assert_called_once_with(1, task)

def test_save_chama_storage_add(mocker):
    """Teste save chama storage.add"""
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Teste", "Desc", Priority.ALTA, prazo)
    
    repo.save(task)
    
    mock_storage.add.assert_called_once()

def test_find_by_id_chama_storage_get(mocker):
    """Teste find_by_id chama storage.get"""
    mock_storage = mocker.Mock()
    mock_storage.get.return_value = "tarefa_mock"
    repo = TaskRepository(mock_storage)
    
    resultado = repo.find_by_id(1)
    
    mock_storage.get.assert_called_once_with(1)
    assert resultado == "tarefa_mock"

def test_find_all_retorna_lista(mocker):
    """Teste find_all retorna lista"""
    mock_storage = mocker.Mock()
    mock_storage.get_all.return_value = ["task1", "task2"]
    repo = TaskRepository(mock_storage)
    
    resultado = repo.find_all()
    
    mock_storage.get_all.assert_called_once()
    assert resultado == ["task1", "task2"]