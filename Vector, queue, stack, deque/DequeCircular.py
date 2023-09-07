import numpy as np 
class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numeroElementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)
    def deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade -1) or (self.inicio == self.final+1)
    def deque_vazio(self):
        return self.inicio == -1
    def insere_inicio(self, valor):
        if self.deque_cheio():
            return -1
        
        # Se estiver vazio 
        if self.deque_vazio():
            self.inicio = 0
            self.final = 0
        elif self.inicio == 0:
            self.inicio = self.capacidade -1
        else:
            self.inicio -=1
        self.valores[self.inicio] = valor
    def insere_final(self, valor):
        if self.deque_cheio():
            return -1
        
        if self.deque_vazio():
            self.inicio = 0 
            self.final = 0
        elif self.final == self.capacidade - 1:
            self.final = 0
        else: self.final += 1
        self.valores[self.final] = valor
    def excluir_inicio(self):
        if self.deque_vazio():
            return -1
        if self.inicio == self.final:
            self.inicio -= 1
            self.final -= 1
        else:
            if self.inicio == self.capacidade-1:
                self.inicio = 0
            else:
                self.inicio += 1
    def excluir_final(self):
        if self.deque_vazio():
            return -1
        if self.inicio == self.final:
            self.inicio -= 1
            self.final -= 1
        elif self.inicio == 0:
            self.final = self.capacidade -1
        else:
            self.final -= 1    
    def get_inicio(self):
        if self.deque_vazio():
            return -1  
        return self.valores[self.inicio]
    def get_final(self):
        if self.deque_vazio():
            return -1  
        return self.valores[self.final]
deque = Deque(5)
deque.insere_final(5)
deque.insere_final(10)
deque.insere_inicio(2)
deque.insere_final(11)

print(deque.get_inicio(), deque.get_final())
    