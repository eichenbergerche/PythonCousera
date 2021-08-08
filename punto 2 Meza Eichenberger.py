gasto_taxi = float(input("ingrese el gasto en taxi: "))
total = 0
while gasto_taxi != 0 and gasto_taxi >= 0:
    total += gasto_taxi
    gasto_taxi = float(input("ingrese el gasto en taxi: "))
print("el total de los gastos en viajes en taxi es: $", total)