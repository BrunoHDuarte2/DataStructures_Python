import numpy as np 
#considerando os valores mais altos como prioritários
class FilaPrioridade:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__qtdElementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)
    def isEmpty(self):
        return self.__qtdElementos == 0
    def isFull(self):
        return self.__qtdElementos == self.__capacidade
    def enqueue(self, valor):
        if self.isFull():
            return -1
        if self.__qtdElementos ==0:
            self.__valores[self.__qtdElementos] = valor
            self.__qtdElementos+=1
        else: 
            x = self.__qtdElementos-1
            while x>=0:
                if valor>self.__valores[x] :
                    self.__valores[x+1] = self.__valores[x]
                else:
                    break
                x-=1
            self.__valores[x+1]=valor
            self.__qtdElementos+=1
    def dequeue(self):
        if self.isEmpty():
            return -1
        for i in range(self.__qtdElementos-1):
            self.__valores[i]=self.__valores[i+1]
        self.__qtdElementos-=1
    def peek(self):
        if self.isEmpty()==False:
            return self.__valores[0]
        else:
            return -1



