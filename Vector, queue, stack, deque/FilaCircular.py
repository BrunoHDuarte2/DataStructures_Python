import numpy as np 
class FilaCircular:
    def __init__(self, capacidade):
        self.__front = 0
        self.__rear = -1
        self.__capacidade = capacidade
        self.__qtdElementos = 0
        self.__valores = np.empty(self.__capacidade, dtype=int)
    def isFull(self):
        return self.__qtdElementos == self.__capacidade
    def isEmpty(self):
        return self.__front == -1
    def enqueue(self, valor):
        if self.isFull():
            return -1
        else:
            self.__qtdElementos +=1
            if self.__rear == self.__capacidade -1:
                self.__rear = 0
            else:
                self.__rear+=1
            self.__valores[self.__rear] = valor 
    def dequeue(self):
        if self.isEmpty():
            return -1
        else: 
            self.__qtdElementos -=1
            if self.__front == self.__capacidade - 1:
                self.__front = 0
            else:
                self.__front += 1
    def peek(self):
        if self.__qtdElementos == 0:
            return
        else:
            print (self.__valores[self.__front])
        return 
    def teste(self):
        for i in range(self.__qtdElementos):
            print(self.__valores[i])


