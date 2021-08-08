#Escribir un programa que pregunte el nombre del usuario 
#en la consola y un número entero e imprima por pantalla en 
# líneas distintas el nombre del usuario tantas veces como 
# el número introducido. Agregué que muestre la cantidad de
# veces que se repitió el nombre.

name = input("¿Me dirías como te llamás?: ")
n = input("Introducí un número entero: ")

print((name + "\n") * int(n),"Tu nombre se repetió", n, "veces.")