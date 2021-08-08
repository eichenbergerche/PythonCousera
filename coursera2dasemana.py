import math
from math import sqrt
c1=2
c2=3
h=sqrt(c1**2+c2**2)
print(h)
#El ejercicio decia que hagamos esto
# c1=2
# c2=3
# h=sqrt(c1**2+c2**2)
# y que digamos el valor de h pero no nos daba mas, a lo que nosotros teniamos que importar la libreria
#y luego utilizar "sqrt" de la misma, lo cual hacemos de la sig. manera "from math (desde la libreria importada)
# importar sqrt (raiz cuadrada)" y luego hacemos que nos muestre el resultado de h con "print(h)"

import random
random = int((random.random()*10)%6+1)
print(random)

a=10
b=12
c=5
print(b*c==6*a)
print(a*b<100)
print(a*b*c>650)
print(a<b<c)

i=3
while i>=0:
    print(i)
    i=i-1

print("finished")

x=1
while x<10:
    if x%2 == 0:
        print(str(x)+" is even")
    else:
        print(str(x)+" is odd")
    x+= 1