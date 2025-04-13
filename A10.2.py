# Ejercicio 2
ahorro, dia = 1, 1

while dia <= 364:
    dia += 1
    ahorro = ahorro + dia
    print("Cantidad ahorrada en el día {} = ${} pesos.".format(dia, ahorro))

print("\nEl ahorro total en el año es: ${} pesos.".format(ahorro))
