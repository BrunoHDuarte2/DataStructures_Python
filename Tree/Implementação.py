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
        self.value = dado
        self.left = None
        self.right = None
    def getValue(self):
        return self.value
class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    def insert_node(self, no_inserido):
        self.root = self.recursion_insert(self.root, no_inserido)
    def recursion_insert(self, no, no_inserido):
        if no is None:
            return no_inserido
        else:
            if no.getValue() > no_inserido.getValue():
                no.left = self.recursion_insert(no.left, no_inserido)
            else:
                no.right = self.recursion_insert(no.right, no_inserido)
        return no
    def inOrder(self):
        lista = []
        self.recursion_in_order(self.root, lista)
        return lista
    def recursion_in_order(self, no, lista):
        if no:
            self.recursion_in_order(no.left, lista)
            lista.append(no.getValue())
            self.recursion_in_order(no.right, lista )
    def preOrder(self):
        lista = []
        self.recursion_pre_order(self.root,lista)
        return lista
    def recursion_pre_order(self, no, lista):
        if no:
            lista.append(no.getValue())
            self.recursion_pre_order(no.left, lista )
            self.recursion_pre_order(no.right, lista )
    def posOrder(self):
        lista = []
        self.recursion_pos_order(self.root, lista)
        return lista
    def recursion_pos_order(self, no, lista ):
        if no:
            self.recursion_pos_order(no.left, lista )
            self.recursion_pos_order(no.right, lista )
            lista.append(no.getValue())
    def largura(self):
        queue = Queue()
        queue.enqueue(self.root)
        self.buscaEmLargura(queue)
    def buscaEmLargura(self, fila):
        while fila.size()!=0:
            no = fila.dequeue()
            if no.left:
                fila.enqueue(no.left)
            if no.right:
                fila.enqueue(no.right)
            print(no.value)
    def larguraAoContrario(self):
        queue = Queue()
        queue.enqueue(self.root)
        lista = self.buscaEmLarguraAoContrario(queue)
        print(lista)
    def buscaEmLarguraAoContrario(self, fila):
        lista = []
        while fila.size()!=0:
            no = fila.dequeue()
            lista.append(no.value)
            if no.left:
                fila.enqueue(no.left)
            if no.right:
                fila.enqueue(no.right)
        return lista[::-1]
            
arvre = BinarySearchTree(Node(20))
arvre.insert_node(Node(15))
arvre.insert_node(Node(25))
arvre.insert_node(Node(27))
arvre.insert_node(Node(22))
arvre.insert_node(Node(14))
arvre.insert_node(Node(16))
arvre.insert_node(Node(1))
arvre.insert_node(Node(2))
print(arvre.inOrder())
print(arvre.preOrder())
print(arvre.posOrder())
arvre.largura()
arvre.larguraAoContrario()