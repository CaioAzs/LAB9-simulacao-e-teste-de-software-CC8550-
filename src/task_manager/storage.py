class InMemoryStorage:
    def __init__(self):
        self._data = {}
    
    def add(self, id, item):
        """Adiciona um item com a chave id"""
        self._data[id] = item
    
    def get(self, id):
        """Retorna o item ou None se não existir"""
        return self._data.get(id)
    
    def get_all(self):
        """Retorna lista com todos os valores"""
        return list(self._data.values())
    
    def delete(self, id):
        """Remove o item e retorna True se removido, False caso contrário"""
        if id in self._data:
            del self._data[id]
            return True
        return False
    
    def clear(self):
        """Limpa todos os dados"""
        self._data.clear()