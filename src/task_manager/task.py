from enum import IntEnum, Enum
from datetime import datetime

class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"

class Task:
    def __init__(self, id, titulo, descricao, prioridade, prazo, status=Status.PENDENTE):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status
    
    def validar(self):
        # Verifica se o título tem pelo menos 3 caracteres
        if len(self.titulo) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres")
        
        # Verifica se o prazo não está no passado
        if self.prazo < datetime.now():
            raise ValueError("Prazo não pode ser no passado")