numero_menor_15 = 0
numero = int(input("ingrese un numero o 0 para salir: "))
while numero != 0:
    numero = int(input("ingrese un numero o 0 para salir: "))
    if numero <= 15:
        numero_menor_15 += 1
print("el total de los numeros menores a 15 es:", numero_menor_15)
