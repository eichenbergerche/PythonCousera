rojo = 0
azul = 0
verde = 0
competidores = 0
tiempo = 0
equipo = 0
while equipo != "fin":
    equipo = str(input("ingrese el equipo del comeptidor (r - rojo | a - azul | v - verde): "))
    if equipo != "r" and equipo != "a" and equipo != "v":
        print("ingrese por favor el equipo correspondinte (r - rojo | a - azul | v - verde)")
    elif equipo == "r":
        rojo += 1
        tiempo = tiempo + float(input("ingrese el tiempo del comeptidor del Area rojo: $"))
        competidores += 1
    elif equipo == "a":
        azul += 1
        tiempo = tiempo + float(input("ingrese el tiempo del comeptidor del Area azul: $"))
        competidores += 1
    elif equipo == "v":
        verde += 1
        tiempo = tiempo + float(input("ingrese el tiempo del comeptidor del Area verde: $"))
        competidores += 1
sueldoprom = tiempo / competidores
print("el total de competidores en la empresa es: ", competidores)
print("el total de competidores en el equipo de rojo es:", rojo)
print("el total de competidores en el equipo de verde es:", verde)
print("el total de competidores en el equipo de azul es:", azul)
print("el tiempo promedio es: $", str(round(sueldoprom, 2)))
