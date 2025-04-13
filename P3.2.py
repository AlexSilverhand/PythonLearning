# Ejercicio 2
numero1 = int(input("Introduzca el primer dato: "))
numero2 = int(input("Introduzca el segundo dato: "))
numero3 = int(input("Introduzca el tercer dato: "))

# Ascendente
if numero1 < numero2 and numero1 < numero3:
    if numero2 < numero3:
        print("\nLos números ingresados en orden ascendente son: {},{},{}".format(
            numero1, numero2, numero3))
    else:
        print("\nLos números ingresados en orden ascendente son: {},{},{}".format(
            numero1, numero3, numero2))
if numero2 < numero1 and numero2 < numero3:
    if numero1 < numero3:
        print("\nLos números ingresados en orden ascendente son: {},{},{}".format(
            numero2, numero1, numero3))
    else:
        print("\nLos números ingresados en orden ascendente son: {},{},{}".format(
            numero2, numero3, numero1))
if numero3 < numero1 and numero3 < numero2:
    if numero1 < numero2:
        print("\nLos números ingresados en orden ascendente son: {},{},{}".format(
            numero3, numero1, numero2))
    else:
        print("\nLos números ingresados en orden ascendente son: {},{},{}".format(
            numero3, numero2, numero1))

# Descendente
if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print("\nLos números ingresados en orden descendente son: {},{},{}".format(
            numero1, numero2, numero3))
    else:
        print("\nLos números ingresados en orden descendente son: {},{},{}".format(
            numero1, numero3, numero2))
if numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print("\nLos números ingresados en orden descendente son: {},{},{}".format(
            numero2, numero1, numero3))
    else:
        print("\nLos números ingresados en orden descendente son: {},{},{}".format(
            numero2, numero3, numero1))
if numero3 > numero1 and numero3 > numero2:
    if numero1 > numero2:
        print("\nLos números ingresados en orden descendente son: {},{},{}".format(
            numero3, numero1, numero2))
    else:
        print("\nLos números ingresados en orden descendente son: {},{},{}".format(
            numero3, numero2, numero1))

else:
    print("Todos los números son iguales")
