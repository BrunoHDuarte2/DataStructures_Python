def BubbleSort(lista):
    for final in range(len(lista), 0, -1):
        haTroca = False
        
        for i in range(0, final-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                haTroca = True
        if not haTroca: 
            break 
lista = [1,2,3,4,5,6]
BubbleSort(lista)
print(lista)  