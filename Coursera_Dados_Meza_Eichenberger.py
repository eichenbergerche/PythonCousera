from random import randint
LanzarOtraVez = True
while LanzarOtraVez == True:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    suma = dado1 + dado2
    print("El primer dado nos arrojó el:", dado1)
    print("El segundo dado nos arrojó el:", dado2)
    print("La suma de los dados nos da:", suma)
    LanzarOtraVez = input("¿Quieres volver a tirar? S/N: ") == "S"
else:
    print("¡Muchas gracias por jugar!")
