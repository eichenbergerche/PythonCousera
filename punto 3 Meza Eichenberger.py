vocales = 0
letras = 0
for letras in range(10):
    letra = str(input("coloque una letra: "))
    letras += 1
    if letra == "a":
        vocales += 1
    elif letra == "e":
        vocales += 1
    elif letra == "i":
        vocales += 1
    elif letra == "o":
        vocales += 1
    elif letra == "u":
        vocales += 1
print("la cantidad de vocales es:", vocales)
