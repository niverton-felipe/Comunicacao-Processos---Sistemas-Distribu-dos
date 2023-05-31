from datetime import datetime
from controlador import Controlador
import random
import time

class Processo:
    def __init__(self, id) -> None:
        self._data_criacao = datetime.now()
        self._id = id
        self._tarefas = {
            1: self._processo1,
            2: self._processo2,
            3: self._processo3
        }

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def destino(self):
        return self.destino
    
    @destino.setter
    def destino(self, value):
        self._destino = value
    
    @property
    def id_tarefa_executada(self):
        return self.id_tarefa_executada
    
    @id_tarefa_executada.setter
    def id_processo_executado(self, value):
        self._id_tarefa_executada = value
    
    def _processo1(self, id_solicitante):
        mensagem = f"Processo {self.id} executando tarefa 1 solicitado pelo id {id_solicitante}"
        print(mensagem)

    def _processo2(self, id_solicitante):
        mensagem = f"Processo {self.id} executando tarefa 2 solicitado pelo id {id_solicitante}"
        print(mensagem)
    
    def _processo3(self, id_solicitante):
        mensagem = f"Processo {self.id} executando tarefa 2 solicitado pelo id {id_solicitante}"
        print(mensagem)
    
    def executar_tarefa_solicitada(self, numero, *args):
        tarefa = self._tarefas.get(numero)
        if tarefa:
            return tarefa(*args)
        else:
            return "Id não encontrado. Acione um processo válido."
    
    def enviar_processo(self, controlador):
        # escolher do processo para envio
        id_destino_igual_origem = True
        while id_destino_igual_origem:
            id_destino = random.randint(0, controlador.numero_processos -1)
            # se id_destino for igual ao id_origem, gera outro id_destino
            if id_destino != self.id:
                id_destino_igual_origem = False

        # escolher aleatoriamente número de tarefas que serão enviadas (máximo de 25 tarefas)
        numero_tarefas_solicitadas = random.randint(1, 25)

        #cria uma lista com uma série de tarefas aleatórias que serão executados pelo processo destino
        lista_tarefas = [random.randint(1, controlador.numero_tarefas) for tarefa in range(numero_tarefas_solicitadas)]
        
        # cria um dicionário com o id_destino do processo e a lista de tarefas que deverão ser executadas
        lista_envio = [id_destino, self.id, lista_tarefas]
        
        return lista_envio

    def receber_processo(self, tarefas, id_solicitante):
        for tarefa in tarefas:
            self.executar_tarefa_solicitada(tarefa, id_solicitante)

if __name__ == "__main__":
    lista_processos = []
    controlador = Controlador()
    fila_tarefas = []

    while True:
        try:
            numero_processos = int(input("Digite o número de processos que serão criados:"))
            if numero_processos > 0 and numero_processos < 1000 :
                print(f"Iniciando o processo de criação dos {numero_processos} processos")
                time.sleep(5)
                print("-"*150)
                break
            else:
                print("Por favor, digite um número inteiro maior que 0 e menor que 1000")
        except ValueError:
            print("Por favor, digite um número inteiro e positivo válido")

    for i in range(numero_processos):
        processo = Processo(i)
        controlador.processo_criado()
        lista_processos.append(processo)
    
    for processo in lista_processos:
        tarefas = processo.enviar_processo(controlador)
        fila_tarefas.append(tarefas) 
    
    for tarefa in fila_tarefas:
        lista_processos[tarefa[0]].receber_processo(tarefa[2], tarefa[1])
        print()




