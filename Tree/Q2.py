class ArvoreBinaria:
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def constituiArvoreBinariaDeBusca(raiz):
    valida = True
    valida = verifica(raiz, valida) * valida
    if valida == 1:
        valida = True
    else:
        valida=False
    return valida
def verifica(raiz, valida):
    if raiz.esq:
        if raiz.dado > raiz.esq.dado:
            valida = verifica(raiz.esq, valida)
        else: valida = False
    if raiz.dir:
        if raiz.dado < raiz.dir.dado:
            valida = verifica(raiz.dir, valida)
        else: valida = False
    return valida

raiz = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
print(constituiArvoreBinariaDeBusca(raiz))