from processo import Processo
from controlador import Controlador
from rpc import Rpc
import time

if __name__ == "__main__":
    lista_processos = []
    controlador = Controlador()
    fila_tarefas = []
    rpc = Rpc()
    uso_rpc = False

    while True:
        try:
            selecao_rpc = int(input(f"Gostaria de utilizar rpc 1-SIM 2-NÃO: \n"))
            if selecao_rpc == 1:
                print("Você escolheu utilizar o RPC para gerenciar a comunicação entre os processos")
                uso_rpc = True
                break
            
            elif selecao_rpc == 2:
                print("Você não utilizará o RPC. Portanto, os processos se comunicarão diretamente\n")
                break
            else:
                print("Por favor, a opção 1 ou 2")
        except ValueError:
            print("Por favor, a opção 1 ou 2")

    
    while True:
        try:
            numero_processos = int(input("Digite o número de processos que serão criados:\n"))
            if numero_processos > 1 and numero_processos < 1000 :
                print(f"Iniciando o processo de criação dos {numero_processos} processos")
                time.sleep(5)
                print("-"*150)
                break
            else:
                print("Por favor, digite um número inteiro maior que 1 e menor que 1000")
        except ValueError:
            print("Por favor, digite um número inteiro e positivo válido")
        


    for i in range(numero_processos):
        processo = Processo(i)
        controlador.processo_criado()
        lista_processos.append(processo)
    
    for processo in lista_processos:
        tarefas = processo.enviar_processo(controlador, uso_rpc)
        if uso_rpc:
            tarefas = rpc.gerenciador_processos(tarefas, controlador)
        fila_tarefas.append(tarefas) 
    
    for tarefa in fila_tarefas:
        lista_processos[tarefa[0]].receber_processo(tarefa[2], tarefa[1], uso_rpc)
        print()
