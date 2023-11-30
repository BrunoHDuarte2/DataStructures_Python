class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)
class BinaryTree:
    def __init__(self):
        self.root = None
    def add_node(self, value):
        self.root = self.recursive_add(self.root, Node(value))   
    def recursive_add(self, root, valueNode):
        if root is None:
            return valueNode
        else:
            if root.value>valueNode.value:
                root.left = self.recursive_add(root.left, valueNode)
            else:
                root.right = self.recursive_add(root.right, valueNode)
        return root
    
    def inOrder(self):
        listaInOrder=[]
        self.recursiveInOrder(self.root, listaInOrder)
        stringInOrder = ''.join([str(x)+" " for x in listaInOrder])
        print(stringInOrder)
    def recursiveInOrder(self, root, lista):
        if root:
            self.recursiveInOrder(root.left, lista)
            lista.append(root)
            self.recursiveInOrder(root.right, lista)
    def preOrder(self):
        listaPreOrder=[]
        self.recursivePreOrder(self.root, listaPreOrder)
        stringPreOrder = ''.join([str(x)+" " for x in listaPreOrder])
        print(stringPreOrder)
    def recursivePreOrder(self, root, lista):
        if root:
            lista.append(root)
            self.recursivePreOrder(root.left, lista)
            self.recursivePreOrder(root.right, lista)
    def posOrder(self):
        listaPosOrder=[]
        self.recursivePosOrder(self.root, listaPosOrder)
        stringPosOrder = ''.join([str(x)+" " for x in listaPosOrder])
        print(stringPosOrder)
    def recursivePosOrder(self, root, lista):
        if root:
            self.recursivePosOrder(root.left, lista)
            self.recursivePosOrder(root.right, lista)
            lista.append(root)
quack = False
tree = BinaryTree()
while not quack:
    leitura = input()
    if leitura == "pre":
        tree.preOrder()
    elif leitura == "in":
        tree.inOrder()
    elif leitura == "pos":
        tree.posOrder()
    elif leitura == "quack":
        quack = True
        break
    else:
        node = int(leitura)
        tree.add_node(node)
            
