# Ejercicio 1
n1 = int(input("Introduzca el primer dato: "))
n2 = int(input("Introduzca el segundo dato: "))
n3 = int(input("Introduzca el tercer dato: "))
n4 = int(input("Introduzca el cuarto dato: "))
n5 = int(input("Introduzca el quinto dato: "))

nMayor = 0
nMenor = 0

# Numero mayor
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    nMayor = n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    nMayor = n2
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    nMayor = n3
elif n4 > n1 and n4 > n3 and n4 > n2 and n4 > n5:
    nMayor = n4
elif n5 > n1 and n5 > n3 and n5 > n4 and n5 > n2:
    nMayor = n5
else:
    print("Los numeros son iguales")

# Numero menor
if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
    nMenor = n1
elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    nMenor = n2
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    nMenor = n3
elif n4 < n1 and n4 < n3 and n4 < n2 and n4 < n5:
    nMenor = n4
elif n5 < n1 and n5 < n3 and n5 < n4 and n5 < n2:
    nMenor = n5
else:
    print("Los numeros son iguales")

print("\nEl número mayor es {} y el menor {}".format(nMayor, nMenor))
