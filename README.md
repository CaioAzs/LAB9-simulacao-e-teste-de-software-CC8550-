# Task Manager

## ⚙️ Instalação
```bash
pip install -r requirements.txt
```

## Executar Testes
```bash
python -m pytest -v
```

### Resultado dos Testes

**Testes de Task:**

![WhatsApp Image 2025-10-16 at 16 02 06_7e6b6845](https://github.com/user-attachments/assets/12a2c0d9-7d84-4a3e-8bae-051b7bc73207)

**Testes de Repository:**

![WhatsApp Image 2025-10-16 at 16 01 50_76d23d0f](https://github.com/user-attachments/assets/e776e69f-0c93-4f47-80f4-2886cbc14a52)


## Exemplo de Uso
```python
from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.storage import InMemoryStorage
from task_manager.repository import TaskRepository

# Criar componentes
storage = InMemoryStorage()
repo = TaskRepository(storage)

# Criar tarefa
prazo = datetime.now() + timedelta(days=5)
task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
task.validar()

# Salvar
task_salva = repo.save(task)
print(f"ID: {task_salva.id}")

# Buscar
encontrada = repo.find_by_id(1)
print(f"Titulo: {encontrada.titulo}")
```
