class No:
    def __init__(self, valor):
        self.info = valor
        self.proximo = None

class FilaListaEncadeada:
    def __init__(self):
        self.primeiro = None 
        self.ultimo = None
    def __lista_vazia(self):
        return self.primeiro == None
    def fila_vazia(self):
        return self.__lista_vazia()
    
    def __insere_final(self, valor):
        no = No(valor)
        if self.__lista_vazia():
            self.primeiro=no
        else:
            self.ultimo.proximo = no
        self.ultimo = no
    def enfileirar(self, valor):
        self.__insere_final(valor)

    def __remover_inicio(self):
        if self.__lista_vazia():
            return 
        else:
            self.primeiro = self.primeiro.proximo
            
    def desenfileirar(self):
        self.__remover_inicio()

    def ver_inicio(self):
        if self.__lista_vazia():
            print("Vazia!")
            return
        print(self.primeiro.info)
fila = FilaListaEncadeada()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.ver_inicio()
