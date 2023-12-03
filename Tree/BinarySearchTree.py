class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def print(self):
        for i in range(self.size()):
            print(f"{self.items[self.size()-i-1].getDado()}", end=', ')
class Node:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
    def getDado(self):
        return self.dado
    def setDado(self, novoDado):
        self.dado = novoDado
    
class BinarySearchTree:
    def __init__(self, noRaiz):
        self.raiz = noRaiz
    def insere(self, noInserido):
        self.raiz = self.insert(self.raiz, noInserido)
    def insert(self, raiz, noInserido):
        if raiz is None:
            return noInserido
        else:
            if raiz.getDado()>noInserido.getDado():
                raiz.esquerda = self.insert(raiz.esquerda, noInserido)
            else:
                raiz.direita = self.insert(raiz.direita, noInserido)
        return raiz
    # Implementação do getAltura()!!!
    def inOrder(self):
        listaInOrder = []
        self.visitaInOrder(self.raiz, listaInOrder)
        return listaInOrder
    def visitaInOrder(self, raiz, lista):
        if raiz:
            self.visitaInOrder(raiz.esquerda, lista)
            #print(raiz.getDado())
            lista.append(raiz.getDado()     )
            self.visitaInOrder(raiz.direita, lista)
    
    def preOrder(self):
        listaPreOrder = []
        self.visitaPreOrder(self.raiz, listaPreOrder)
        return listaPreOrder
    def visitaPreOrder(self, raiz, lista):
        if raiz:
            #print(raiz.getDado())
            lista.append(raiz.getDado())
            self.visitaPreOrder(raiz.esquerda, lista)
            self.visitaPreOrder(raiz.direita, lista)
    def posOrder(self):
        listaPosOrder = []
        self.visitaInOrder(self.raiz, listaPosOrder)
        return listaPosOrder
    def visitaPosOrder(self, raiz, lista):
        if raiz:
            self.visitaPosOrder(raiz.esquerda, lista)
            self.visitaPosOrder(raiz.direita, lista)
            lista.append(raiz.getDado())   
    def largura(self):
        fila = Queue()
        fila.enqueue(self.raiz)
        lista = self.visitaLarguraIterativo(self.raiz, fila)
        print(lista) 
    def visitaLarguraIterativo(self, raiz, fila):
        listaResultado = []
        while fila.size()!=0:
            noAtual = fila.dequeue()
            listaResultado.append(noAtual.getDado())
            
            if noAtual.esquerda:
                fila.enqueue(noAtual.esquerda)
            if noAtual.direita:
                fila.enqueue(noAtual.direita)
        return listaResultado
    def larguraAoContrario(self):
        fila = Queue()
        fila.enqueue(self.raiz)
        lista = self.visitaLarguraIterativoAoContratrio(self.raiz, fila)
        print(lista)
    def visitaLarguraIterativoAoContratrio(self, raiz, fila):
        listaResultado = []
        while fila.size()!=0:
            noAtual = fila.dequeue()
            listaResultado.append(noAtual.getDado())
            if noAtual.esquerda:
                fila.enqueue(noAtual.esquerda)
            if noAtual.direita:
                fila.enqueue(noAtual.direita)
        # Nesse caso é retornado a lista ao contrário, com os valores da direita para a esquerda
        # Caso seja necessário os valores da esquerda para a direita é só inverter os dois if's acima
        return listaResultado[::-1]
    ## LARGURA AO CONTRÁRIO = Possível questão da prova 


arvre = BinarySearchTree(Node(20))
arvre.insere(Node(15))
arvre.insere(Node(25))
arvre.insere(Node(27))
arvre.insere(Node(22))
arvre.insere(Node(14))
arvre.insere(Node(16))
arvre.insere(Node(1))
arvre.insere(Node(2))


print(arvre.inOrder())     
print(arvre.preOrder())  
print(arvre.posOrder())     
arvre.largura()
arvre.larguraAoContrario()