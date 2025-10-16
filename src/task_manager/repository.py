class TaskRepository:
    def __init__(self, storage):
        self.storage = storage
        self._next_id = 1
    
    def save(self, task):
        """Atribui ID, salva no storage e retorna a task"""
        task.id = self._next_id
        self._next_id += 1
        self.storage.add(task.id, task)
        return task
    
    def find_by_id(self, id):
        """Busca e retorna a task ou None"""
        return self.storage.get(id)
    
    def find_all(self):
        """Retorna lista de todas as tasks"""
        return self.storage.get_all()
    
    def delete(self, id):
        """Remove a task"""
        return self.storage.delete(id)