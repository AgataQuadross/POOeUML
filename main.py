import os
from datetime import date

class Atividades:

    def __init__(self, nome_atividade, descricao, data_entrega, nota):
        self.__nome_atividade = nome_atividade
        self.__descricao = descricao
        self.__data_entrega = data_entrega
        self.__nota = nota

    def lancar_atividade(self):
        lanca = self
        
        if lanca == "s" or lanca == "S":
            print("Enviando atividade...")
        elif lanca == "n" or lanca == "N":
            print("Ok! descartando atividade")
            exit()
        else:
            print("Opção invalida, assumindo resposta positiva")
    def exibir_atividade(self):
        print("~*" * 20)
        print(f"{self.__nome_atividade} - {self.__data_entrega}")
        print(f"{self.__nota}")
        print("*-" * 10)
        print(f"{self.__descricao}")
        print("~*" * 20)


os.system('cls')

nome = str(input("Nome da sua atividade: "))
descricao = str(input("descreva a sua atividade(instruções, prompt, etc): "))
nota = float(input("quanto vale essa atividade? "))
data = str(input("qual a data de entrega? "))

informacoes = Atividades(nome, descricao, data, nota)

resposta = str(input("Deseja enviar essa atividade?(s/n): "))

Atividades.lancar_atividade(resposta)

Atividades.exibir_atividade(informacoes)
