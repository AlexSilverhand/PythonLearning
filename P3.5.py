# Ejercicio 5
horasTotales = float(input("\nIntroduzca las horas trabajadas: "))
horasExtra = 0
horasExtra2 = 0
pagoNormal = float(input("\nIntroduzca el pago por hora: "))
pagoTotal = 0

if horasTotales <= 40:
    pagoTotal = pagoNormal*horasTotales
elif horasTotales > 40:
    horasExtra = horasTotales-40
    if horasExtra <= 8:
        pagoTotal = (pagoNormal*40) + (pagoNormal*2*horasExtra)
    elif horasExtra > 8:
        horasExtra2 = horasTotales-48
        pagoTotal = (pagoNormal*40) + (pagoNormal*2*8) + \
            (pagoNormal*3*horasExtra2)
print("\nSu sueldo por {} horas trabajadas esta semana es de {} pesos".format(
    horasTotales, pagoTotal))
