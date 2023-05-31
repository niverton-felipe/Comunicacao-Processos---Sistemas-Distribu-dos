class Controlador:
    def __init__(self,) -> None:
        self._numero_processos = 0
        self._numero_tarefas = 3
    
    @property
    def numero_processos(self):
        return self._numero_processos
    
    @property
    def numero_tarefas(self):
        return self._numero_tarefas
    
    def processo_criado(self):
        self._numero_processos += 1
