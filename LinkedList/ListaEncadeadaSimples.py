import numpy as np 
class No:
    def __init__(self, info):
        self.info = info
        self.ponteiro = None
    def mostra_no(self):
        print(self.info)
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None 
    def insere_inicio(self, info):
        no = No(info)
        no.ponteiro = self.primeiro
        self.primeiro = no 
    
    def excluir_inicio(self):
        excluido = self.primeiro 
        if self.primeiro.ponteiro == None:
            self.primeiro = None
            return None
        self.primeiro = self.primeiro.ponteiro
        return excluido
    def pesquisa(self, info):
        if self.primeiro == None:
            return
        contador = self.primeiro
        while contador != None:
            if contador.info == info:
                return contador
            contador = contador.ponteiro
        return None
    def excluir_posicao(self, info):
        if self.primeiro == None:
            return
        if self.primeiro.info == info:
            self.excluir_inicio()
        atual = self.primeiro
        anterior = self.primeiro
        while atual != None:
            if atual.info == info:
                anterior.ponteiro = atual.ponteiro
                return
            if atual == anterior:
                atual = atual.ponteiro
            else: 
                atual = atual.ponteiro 
                anterior = anterior.ponteiro
    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.ponteiro
lista = ListaEncadeada()
lista.insere_inicio(6)
lista.insere_inicio(5)
lista.insere_inicio(4)
lista.insere_inicio(3)
lista.insere_inicio(2)
lista.insere_inicio(1)
lista.mostrar()


