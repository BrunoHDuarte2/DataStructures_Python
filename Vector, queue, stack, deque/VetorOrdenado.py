import numpy as np
class VetorOrdenado:
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
            return 
        
        posicao = 0
        for i in range(self.ultimaPosicao+1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultimaPosicao:
                posicao = i+1

        x = self.ultimaPosicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x] 
            x-=1

        self.valores[posicao] = valor
        self.ultimaPosicao +=1
    def pesquisa(self, valor):
        for i in range(self.ultimaPosicao+1):
            if self.valores[i]> valor:
                return -1
            if self.valores[i] == valor:
                return i 
    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao+1):
                self.valores[i] = self.valores[i+1]
            self.ultimaPosicao -=1
    def binaySearch(self, valor):
        lim0 = 0
        limS = self.ultimaPosicao
        while True:
            posicao_atual = int((lim0+limS)/2)
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif lim0 > limS:
                return -1   
            else:
                if self.valores[posicao_atual] < valor:
                    lim0 = posicao_atual+1
                else:
                    limS = posicao_atual+1 



vetor = VetorOrdenado(10)
vetor.insere(14)
vetor.insere(42)
vetor.insere(52)
vetor.insere(106)
vetor.insere(5)
vetor.insere(9)
vetor.insere(56)
vetor.insere(73)
vetor.insere(90)
vetor.insere(1)
vetor.imprime()
print("-----------------------------")
print(vetor.binaySearch(20))
         
