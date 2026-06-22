import os
from datetime import date

class Atividades:

    def __init__(self, nome_atividade, descricao, data_entrega, nota):
        self.__nome_atividade = nome_atividade
        self.__descricao = descricao
        self.__data_entrega = data_entrega
        self.__nota = nota

    def lancar_atividade(self):
        lanca = input(string("Deseja enviar essa atividade?(s/n): "))
        
        if lanca == "s" or lanca == "S":
            print("Enviando atividade...")
        elif lanca == "n" or lanca == "N":
            print("Ok! descartando atividade")
        else:
            print("Opção invalida, assumindo resposta positiva")

    def exibir_atividade(self):
print("{self.__nome_atividade} - {self.__data_entrega}")
        print("{self.__nota}")
        print("{self.__descricao}")


os.system('cls')

nome = Atividades.nome_atividade(input(string("Nome da sua atividade: "))
descricao = Atividades.descricao(input(string("descreva a sua atividade(instruções, prompt, etc): "))
nota = Atividades.nota(input(float("quanto vale essa atividade? "))
data = Atividades.data_entrega(input(float("qual a data de entrega? "))

