def quickSort(lista):
    quickSortHelper(lista, 0, len(lista)-1)
def quickSortHelper(lista, primeiro, ultimo):
    if primeiro<ultimo:
        pontoDeTroca = partition(lista, primeiro, ultimo)
        quickSortHelper(lista, primeiro, pontoDeTroca-1)
        quickSortHelper(lista, pontoDeTroca+1, ultimo)
def partition(lista, primeiro, ultimo):
    pivo = lista[primeiro]
    esquerda = primeiro+1
    direita = ultimo 
    ok = False
    while not ok:
        while esquerda<=direita  and lista[esquerda]<=pivo:
            esquerda+=1
        while direita>=esquerda and lista[direita]>=pivo:
            direita-=1
        if esquerda>direita:
            ok = True
        else:
            
            lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
    lista[primeiro], lista[direita] = lista[direita], lista[primeiro]
    return direita

lista= [23,4,25,56,2,51,7,2,6,7]
quickSort(lista)
print(lista)