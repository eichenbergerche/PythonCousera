infantil = 0
joven = 0
adulto = 0
veterano = 0
competidores = 0
tiempo = 0
categoria = 0
while categoria != "fin":
    categoria = str(input("ingrese la categoria del competidor (i - infantil | j - joven | a - adulto | v - veterano): "))
    if categoria != "i" and categoria != "j" and categoria != "a" and categoria != "v":
        print("---ingrese por favor el categoria correspondinte (i - infantil | j - joven | a - adulto | v - veterano)---")
    elif categoria == "i":
        infantil += 1
        tiempo = tiempo + float(input("ingrese el tiempo del competidor en la categoria infantil: "))
        competidores += 1
    elif categoria == "j":
        joven += 1
        tiempo = tiempo + float(input("ingrese el tiempo del competidor en la categoria joven: "))
        competidores += 1
    elif categoria == "a":
        adulto += 1
        tiempo = tiempo + float(input("ingrese el tiempo del competidor en la categoria adulto: "))
        competidores += 1
    elif categoria == "v":
        veterano += 1
        tiempo = tiempo + float(input("ingrese el tiempo del competidor en la categoria veterano: "))
        competidores += 1
tiempo_prom = tiempo / competidores
print("el total de competidores es: ", competidores)
print("el total de competidores en la categoria infantil es:", infantil)
print("el total de competidores en la categoria adulto es:", adulto)
print("el total de competidores en la categoria joven es:", joven)
print("el total de competidores en la categoria veterano es:", veterano)
print("el tiempo promedio es:", str(round(tiempo_prom, 2)))