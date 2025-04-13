print("---------¡Bienvenido!---------")
print("\n1. De Celsius ℃ a Farenheit ℉")
print("2. De Celsius ℃ a Kelvin °K")
print("3. De Farenheit ℉ a Celsius ℃")
print("4. De Kelvin °K a Celsius ℃")

opcion = int(input("\nSeleccione una opción: "))


if opcion == 1:
    print("\nDe Celsius ℃ a Farenheit ℉")
    grados = float(input("\nIngrese la temperatura en grados Celsius: "))
    conversion = (grados * 9/5) + 32
    print("{} grados Celsius equivalen a {} grados Farenheit".format(
        grados, conversion))

elif opcion == 2:
    print("\nDe Celsius ℃ a Kelvin °K")
    grados = float(input("\nIngrese la temperatura en grados Celsius: "))
    conversion = grados + 273.15
    print("{} grados Celsius equivalen a {} grados Kelvin".format(grados, conversion))

elif opcion == 3:
    print("\nDe Farenheit ℉ a Celsius ℃")
    grados = float(input("\nIngrese la temperatura en grados Farenheit: "))
    conversion = (grados - 32) * 5/9
    print("{} grados Farenheit equivalen a {} grados Celsius".format(
        grados, conversion))

elif opcion == 4:
    print("\nDe Kelvin °K a Celsius ℃")
    grados = float(input("\nIngrese la temperatura en grados Kelvin: "))
    conversion = grados - 273.15
    print("{} grados Kelvin equivalen a {} grados Celsius".format(grados, conversion))

else:
    print("\nOpción no válida")
