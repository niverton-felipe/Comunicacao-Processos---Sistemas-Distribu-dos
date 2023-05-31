class Controlador:
    def __init__(self, numero_processos, numero_tarefas) -> None:
        self._numero_processos = numero_processos
        self._numero_tarefas = numero_tarefas
    
    @property
    def numero_processos(self):
        return self._numero_processos
    
    @property
    def numero_tarefas(self):
        return self._numero_tarefas
    
    def processo_criado(self):
        self._numero_processos += 1
