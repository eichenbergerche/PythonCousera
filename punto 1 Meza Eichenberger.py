suma = 0
for semana in range(7):
    temp= float(input("Escriba la temperatura del día: "))
    suma = suma + temp
prom = suma / semana
print("El promedio de las temperaturas es:", str(round(prom, 2)))