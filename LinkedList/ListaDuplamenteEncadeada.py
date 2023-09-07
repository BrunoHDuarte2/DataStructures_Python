class No:
    def __init__(self, info):
        self.valor = info
        self.proximo = None
        self.anterior = None 
    def mostra_no(self):
        print(self.valor)
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        no = No(valor)
        if self.__lista_vazia():
            self.ultimo = no 
        else:
            self.primeiro.anterior = no
        no.proximo = self.primeiro 
        self.primeiro = no 
    
    def insere_final(self, valor):
        no = No(valor)
        if self.__lista_vazia():
            self.primeiro = no
            self.ultimo = no 
        else: 
            self.ultimo.proximo = no 
            no.anterior = self.ultimo
        self.ultimo = no
    def excluir_inicio(self):
        if self.__lista_vazia():
            return
        if self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None 
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
    def excluir_final(self):
        if self.__lista_vazia():
            return
        self.ultimo.anterior.proximo = None
    def excluir_posicao(self, valor):
        no = self.primeiro
        while no!=None:
            if no.valor == valor:
                no.anterior.proximo = no.proximo
                no.proximo.anterior = no.anterior
            no = no.proximo
            
    def mostrar(self):
        no = self.primeiro
        while no!=None:
            no.mostra_no()
            no = no.proximo
    
lista = ListaDuplamenteEncadeada()
lista.insere_inicio(3)
lista.insere_inicio(2)
lista.insere_inicio(1)
lista.insere_final(4)
lista.insere_final(5)
lista.insere_final(6)
lista.excluir_posicao(4)
lista.mostrar()