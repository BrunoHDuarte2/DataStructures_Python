class ArvoreBinaria:
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir 
def verificaSimetria(raiz):
    if raiz is None:
        return True
    return valida(raiz.esq, raiz.dir)
def valida(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    return (left.dado == right.dado) and valida(left.esq, right.dir) and valida(left.dir, right.esq)

    
raiz = ArvoreBinaria(0, ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)), ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)))
print(verificaSimetria(raiz))