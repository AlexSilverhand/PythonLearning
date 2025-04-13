# Ejercicio 3
year = int(input("Introduzca el año: "))

if not year % 4 and (year % 100 or not year % 400):
    print("El año {} es bisiesto".format(year))
else:
    print("El año {} no es bisiesto".format(year))
