import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    def imprime(self):
        if self.ultimaPosicao ==-1:
            print('O vetor está vázio')
        else: 
            for i in range(self.ultimaPosicao+1):
                print(i, '-', self.valores[i])
    def insere(self, valor):
        if self.ultimaPosicao == self.capacidade -1:
            print('Capacidade máxima atingida')
        else: 
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor
    def pesquisaLinear(self, valor):
        for i in range(self.ultimaPosicao +1):
            if valor == self.valores[i]:
                return i
        return -1
    def excluir(self, valor):
        posicao = self.pesquisaLinear(valor)
        if posicao == -1:
            return -1
        else: 
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i+1]
            self.ultimaPosicao -= 1
