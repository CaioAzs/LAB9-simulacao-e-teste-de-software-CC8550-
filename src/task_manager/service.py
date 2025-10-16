from task_manager.task import Task, Status

class TaskService:
    def __init__(self, repository):
        self.repository = repository
    
    def criar_tarefa(self, titulo, descricao, prioridade, prazo):
        """Cria, valida e salva uma tarefa"""
        task = Task(None, titulo, descricao, prioridade, prazo)
        task.validar()
        return self.repository.save(task)
    
    def listar_todas(self):
        """Retorna todas as tarefas"""
        return self.repository.find_all()
    
    def atualizar_status(self, id, status):
        """Atualiza o status de uma tarefa"""
        task = self.repository.find_by_id(id)
        if task:
            task.status = status
            return task
        return None