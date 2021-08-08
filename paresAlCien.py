maximo = int(input("Por favor ingresar el valor máximo: "))
total = 0

for numero in range(1, maximo +1):
    if (numero % 2 == 0):
        print("{0}".format(numero))
        total = total + numero
print("La suma de los números pares desde 1 a {0} = {1}". format(numero, total))
