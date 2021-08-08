def calcPerimetroTriangulo (a, b, c):
    perimetro = a + b + c
    return perimetro
print("Ingrese el valor del primer lado")
lado1 = int(input())
print("Ingrese el valor del segundo lado")
lado2 = int(input())
print("Ingrese el valor del tercer lado")
lado3 = int(input())
perimetroTriangulo = calcPerimetroTriangulo(lado1, lado2, lado3)
print("El perimetro del triángulo de lados", lado1,",", lado2," y", lado3, "es:", perimetroTriangulo)