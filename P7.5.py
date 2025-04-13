lista = [1, 1, 2, 34, 5, 6, 7, 8, 8, 9, 10, 11, 24, 0, 2]
listaM = []
listaSR = []
print('Lista original =', lista)

for i in lista:
    if i < 10:
        listaM.append(i)
    if not i in listaSR:
        listaSR.append(i)

print(print('Lista menores de 10 =', listaM))
print(print('Lista sin elementos repetidos =', listaSR))
