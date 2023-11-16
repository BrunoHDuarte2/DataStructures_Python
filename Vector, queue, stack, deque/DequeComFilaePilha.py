# Insere Final e remove Final (LIFO)
class Pilha:
    def __init__(self):
        self.itens = []
    def isEmpty(self):
        return self.itens == []
    def push(self, item):
        return self.itens.append(item)
    def pop(self):
        if self.isEmpty():
            return "Pilha Vazia"
        return self.itens.pop()
    def peek(self):
        if self.isEmpty():
            return "Pilha Vazia"
        return self.itens[len(self.itens)-1]
    def size(self):
        return len(self.itens)
    def getItens(self):
        return self.itens
    def setItens(self, parametro):
        self.itens = parametro
    def verPilha(self):
        for i in range(self.size()):
            print(self.itens[i])
# Insere Inicio e Remove Final (FIFO)
class Fila:
    def __init__(self):
        self.itens = []
    def isEmpty(self):
        return self.itens == []
    def enqueue(self, item):
        return self.itens.insert(0, item)
    def dequeue(self):
        if self.isEmpty():
            return "Fila Vazia"
        return self.itens.pop()
    def peek(self):
        if self.isEmpty():
            return "Fila Vazia"
        return self.itens[0]
    def size(self):
        return len(self.itens)
    def getItens(self):
        return self.itens
    def setItens(self, parametro):
        self.itens = parametro
    def verFila(self):
        for i in range(self.size()):
            print(self.itens[i])
class Deque:
    def __init__(self):
        self.pilha = Pilha()
        self.fila = Fila()
    # Insere no inicio
    # usando enqueue, já que a fila que estou usando insere no inicio e remove no final 
    def enqueue(self, item):
        self.fila.enqueue(item)
        self.pilha.setItens(self.fila.getItens())  
    # Usando push já que a pilha já insere no final 
    def push(self, item):
        self.pilha.push(item) 
        self.fila.setItens(self.pilha.getItens()) 
    def verDeque(self):
        for i in range(self.pilha.size()):
            valores = self.pilha.getItens()
            print(valores[i])
    # Remove 
    def removePrimeiro(self):
        self.pilha.getItens().pop(0)
        self.fila.setItens(self.pilha.getItens())
    def pop(self):
        self.pilha.pop()
        self.fila.setItens(self.pilha.getItens())
        

    

deque = Deque()
deque.push(1)
deque.push(2)
deque.push(3)
deque.push(4)
deque.enqueue(0)

deque.pop()
deque.removePrimeiro()
deque.removePrimeiro()


deque.verDeque()

            
        

