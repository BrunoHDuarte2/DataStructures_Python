class Node:
    def __init__(self, info):
        self.info = info 
        self.prox = None
    def mostra(self):
        print(self.info)
class LinkedList:
    def __init__(self):
        self.primeiro = None
    def insereInicio(self, info):  
        if self.primeiro == None:
            self.primeiro = Node(info)
        else:
            no = Node(info)
            no.prox = self.primeiro
            self.primeiro = no
    def excluirInicio(self):
        if self.primeiro == None:
            pass
        else:
            self.primeiro = self.primeiro.prox
    def inserirFinal(self, info):
        no = self.primeiro
        while no != None:
            if no.prox == None:
                no.prox = Node(info)
            no = no.prox
    def showList(self):
        no = self.primeiro
        while no!=None:
            no.mostra()
            no = no.prox
lista = LinkedList()    
lista.insereInicio(4)
lista.insereInicio(3)
lista.insereInicio(2)
lista.insereInicio(1)
lista.inserirFinal(5)
lista.showList()