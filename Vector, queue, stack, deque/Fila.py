import numpy as np 
class Fila:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__ultimo = -1
        self.__valores = np.empty(self.__capacidade , dtype=int)
    def filaVazia(self):
        if self.__ultimo == -1:
            return True
        else: 
            return False
    def filaCheia(self):
        if self.__ultimo == self.__capacidade - 1:
            return True
        else:
            return False
    def enfileirar(self, valor):
        if self.filaCheia():
            return -1
        else:
            self.__ultimo += 1
            self.__valores[self.__ultimo] = valor
    def desenfileirar(self):
        if self.filaVazia():
            return -1
        else:
            for i in range(self.__ultimo):
                self.__valores[i] = self.__valores[i+1]
            self.__ultimo-=1
    def primeiroDaFila(self):
        if self.filaVazia():
            return "Não há primeiro"
        else: 
            return self.__valores[0]

