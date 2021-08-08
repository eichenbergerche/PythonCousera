print("¿Cuantos números necesita para el promedio?")
numNecesarios = int(input())
contador = 1
sumatoria = 0
while contador <= numNecesarios:
    print("Ingrese un número: ")
    num = float(input())
    sumatoria = sumatoria + num
    contador = contador + 1
promedio = sumatoria / numNecesarios
print("El promedio de los números ingresados es:", promedio)