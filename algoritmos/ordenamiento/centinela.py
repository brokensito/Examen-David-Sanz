
"""Busca un elemento que esta dentro de una lista"""

def centinela(lista,buscado):
    
    posicion = -1
    i = 0

    while (i < len(lista)) and (posicion == -1):
        if (lista[i]==buscado):
            posicion = i
        i += 1

    return posicion


print(centinela([1,2,4,5,551,2,2], 2))


