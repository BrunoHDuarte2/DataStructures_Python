class No:
    def __init__(self, valor):
        self.info = valor
        self.proximo = None
    def mostra_no(self):
        print(self.info)
class PilhaListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def __lista_vazia(self):
        return self.primeiro == None
    def pilha_vazia(self):
        return self.__lista_vazia()

    def __insere_inicio(self, valor):
        no = No(valor)
        if self.__lista_vazia():
            self.primeiro = no 
        else: 
            no.proximo = self.primeiro
            self.primeiro = no
    def empilha(self, valor):
        #usa do método de inserção no inicio, de onde será retirada os elementos
        self.__insere_inicio(valor)

    def __remove_inicio(self):
        if self.__lista_vazia():
            return
        else:
            self.primeiro = self.primeiro.proximo
    def desempilhar(self):
        self.__remove_inicio()

    def ver_topo(self):
        if self.__lista_vazia():
            print("Vazia!")
        else:
            print(self.primeiro.info)