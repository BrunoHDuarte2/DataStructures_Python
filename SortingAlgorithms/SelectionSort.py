def SelectionSort(lista):
    for final in range(len(lista), 0, -1):
        posMaior = 0
        for i in range(final):
            if lista[posMaior] < lista[i]:
                posMaior = i
        lista[final-1], lista[posMaior] = lista[posMaior], lista[final-1] 
        
lista = [75, 23, 52, 12, 1, 4, 2, 90, 70, -4, 43, -15]
SelectionSort(lista)
print(lista) 