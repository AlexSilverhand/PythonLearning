# Ejercicio 5
print("Los múltiplos de 9 que se encuentran desde 45 hasta 194 son:\n")
sum = 0
cont = 45
cont2 = 0
while cont <= 194:
    print(cont)
    sum = sum + cont
    cont = cont + 9
    cont2 = cont2 + 1
prom = sum / cont2
print("\nLa suma de todos los múltiplos es: ", sum)
print("El promedio los múltiplos es: ", prom)
