# Ejerciio 6
horas = int(input("\nIngrese la cantidad de horas: "))
minutos = int(input("\nIngrese la cantidad de minutos: "))
horasT = 0
horas10 = 0
horasdesc = 0
precio = 0
descuento = 0

horasasegundos = horas * 3600
minutosasegundos = minutos * 60
tiempo = horasasegundos + minutosasegundos

if tiempo <= 600:
    precio = 0
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))

elif tiempo > 600 and tiempo <= 1800:
    precio = 6
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))

# más de 30 minutos a 1 hora
elif tiempo > 1800 and tiempo <= 3600:
    precio = 15
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))

# 1 hora a 4 horas
elif (tiempo >= 3600 and tiempo <= 14400) and minutos == 0:
    precio = horas * 15
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))
elif (tiempo >= 3600 and tiempo <= 14400) and minutos != 0:
    horasT = horas + 1
    precio = horasT * 15
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))

# 4 hora a 10 horas
elif (tiempo > 14400 and tiempo <= 36000) and minutos == 0:
    horas10 = horas - 4
    precio = 60 + (horas10*10)
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))
elif (tiempo > 14400 and tiempo <= 36000) and minutos != 0:
    horasT = horas + 1
    horas10 = horasT - 4
    precio = 60 + (horas10*10)
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))

# Más de 10 horas
elif (tiempo > 36000) and minutos != 0:
    horasT = horas + 1
    horas10 = horasT - 4
    horasdesc = 60 + (horas10*10)
    descuento = (horasdesc*20)/100
    precio = horasdesc - descuento
    print("El precio a pagar por {} horas y {} minutos de estacionamiento es ${} pesos.".format(
        horas, minutos, precio))
