class No:
    def __init__(self, info):
        self.info = info
        self.ponteiro = None
    def mostra_no(self):
        print(self.info)
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def __lista_vazia(self):
        return self.primeiro == None
    def insere_inicio(self, valor):
        no = No(valor)
        if self.__lista_vazia():
            self.ultimo = no
        no.ponteiro = self.primeiro
        self.primeiro = no
    def insere_final(self, valor):
        no = No(valor)
        if self.__lista_vazia():
            self.primeiro=no
        else:
            self.ultimo.ponteiro = no
        self.ultimo = no
    def excluir_inicio(self):
        if self.__lista_vazia():
            return
        self.primeiro = self.primeiro.ponteiro
    def listagem(self):
        no = self.primeiro 
        while no!=None:
            no.mostra_no()
            no = no.ponteiro


            
