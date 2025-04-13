# Ejercicio 3

cont = 1
alumnosA = 0
alumnosR = 0
alumnos = int(input("Ingrese la cantidad de alumnos: "))

while cont <= alumnos:
    cal = int(input("Ingrese la calificación del alumno {}: ".format(cont)))
    if cal >= 60 and cal <= 100:
        alumnosA += 1
        cont += 1
    elif cal < 60 and cal >= 0:
        alumnosR += 1
        cont += 1
    else:
        print("Calificación no válida, intentelo de nuevo.")

print("\nEn su clase hay {} alumnos, de los cuales {} están aprobados y {} reprobados.".format(
    alumnos, alumnosA, alumnosR))
