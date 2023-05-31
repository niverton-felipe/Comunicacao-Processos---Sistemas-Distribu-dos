import random

class Rpc:
    def gerenciador_processos(self,lista_processos, controlador):
        id_origem = lista_processos[1]
        id_destino = self._escolher_id_destino(id_origem, controlador)
        # se RCP for chamado, ele substituirá o Id destino Fake, pelo que foi escolhido na linha anterior.
        lista_processos[0] = id_destino
        return lista_processos
    
    def _escolher_id_destino(self, id_origem, controlador):
        # escolher do processo para envio
        id_destino_igual_origem = True
        while id_destino_igual_origem:
            id_destino = random.randint(0, controlador.numero_processos -1)
            # se id_destino for igual ao id_origem, gera outro id_destino
            if id_destino != id_origem:
                id_destino_igual_origem = False
        return id_destino
