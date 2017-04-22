#Organize os elementos de uma lista em ordem crescente

lista = [4, 3, 1, 6, 7, 2, 5]
aux = lista[:]
lista2 = []

print("Antes : ", lista)
"""
while len(lista2) != len(lista):
    menor = aux[0]
    for elemento in aux:
        if elemento < menor:
            menor = elemento

    lista2.append(menor)
    aux.remove(menor)

lista = lista2
print("Depois: ", lista)
"""

#metodo Python
lista.sort()
print("Depois: ", lista)

#metodo clear() remove todos os elementos da lista
#metodo copy() copia os elementos de uma lista