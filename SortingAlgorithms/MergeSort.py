def MergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        left = lista[:meio]
        right = lista[meio:]
        MergeSort(left)
        MergeSort(right)

        topoLeft = 0
        topoRight=0
        topoLista=0
        while topoLeft < len(left) and topoRight < len(right):
            if left[topoLeft] < right[topoRight]:
                lista[topoLista] = left[topoLeft]
                topoLeft+=1
            else:
                lista[topoLista] = right[topoRight]
                topoRight+=1
            topoLista+=1
        
        while topoLeft < len(left):
            lista[topoLista] = left[topoLeft]
            topoLeft+=1
            topoLista+=1
        while topoRight < len(right):
            lista[topoLista] = right[topoRight]
            topoRight+=1
            topoLista+=1
lista = [23,4 ,3 ,25,45,6,3,8,9,24, 64, 302, 53]
MergeSort(lista)
print(lista)