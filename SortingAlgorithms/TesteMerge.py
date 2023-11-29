def MergeSort(lista):
    if len(lista)>1:
        esquerda = lista[:len(lista)//2]
        direita = lista[len(lista)//2:]
        MergeSort(esquerda)
        MergeSort(direita)
        i,j,k =0,0,0
        while i < len(esquerda) and j <len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i+=1
            else:
                lista[k] = direita[j]
                j+=1
            k+=1
        while i<len(esquerda):
            lista[k] = esquerda[i]
            i+=1
            k+=1
        while j<len(direita):
            lista[k] = direita[j]
            j+=1
            k+=1

lista = [4,6,12,7,2,7,9,1]
MergeSort(lista)
print(lista)