import numpy as np
class PilhaD:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.chararray(self.__capacidade , unicode=True)
    def __pilha_cheia(self): 
        if self.__topo == self.__capacidade-1:
            return True
        else: 
            return False
    def pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False
    def empilhar(self, valor):
        if self.__pilha_cheia():
            return -1
        else: 
            self.__topo += 1
            self.__valores[self.__topo] = valor
    def desempilhar(self):
        if self.pilha_vazia():
            return -1
        else: 
            valor = self.__valores[self.__topo]
            self.__topo -=1
            return valor
    def ver_topo(self):
        if self.pilha_vazia():
            return -1
        else: 
            return self.__valores[self.__topo]
        
texto = "a{b(c[d]e)f}"
pilha = PilhaD(len(texto))
for i in range(len(texto)):
    pilha.ver_topo()
    char = texto[i]
    if char == '{' or char == '(' or char == '[':
        pilha.empilhar(char)
    else:
        if char == ')' or char == '}' or char == ']':
            if pilha.ver_topo() == '(' and char == ')':   
                pilha.desempilhar()
            if pilha.ver_topo() == '{' and char == '}':
                pilha.desempilhar()
            if pilha.ver_topo() == '[' and char == ']':
                pilha.desempilhar()
            else: 
                print("ERRO!")
    
