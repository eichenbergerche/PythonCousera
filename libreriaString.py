import string

name = "Charles Henry"
formatter = string.Formatter()
formatter.format("Hola {}", name)
print("Hola {}!, ¿que tal el noviazgo?".format(name))
print("{} + {} = {}".format(2, 5, 7))
print("{1} + {2} = {0}".format(7, 5, 2)) #"5 + 2 = 7"
print("Hola {name}".format(name = name)) #"Hola Charles Henry"
print("{0} + {1} = {result}".format(9, 5, result=14)) #"9 + 5 = 14"

tupla = (4, 3)
print("X:{0[0]}; Y:{0[1]}".format(tupla)) #"X: 4; Y: 3"
print("{0:f} + {1:f} = {result:f}".format(2, 5, result=7)) #"2.000000 + 5.000000 = 7.000000"
print("{0:.3f} + {1:.3f} = {result:.3f}".format(4, 6, result=10)) #"2.000 + 5.000 = 7.000"
print("{:d}".format(25)) #"25"
print("{2} - {0} - {1}".format(1,2,3))
print("{:d}".format(2.5))
print("{:*^10}".format("prueba"))

nro_cuenta = "32673"
saldo = 100.2543
#¿Como le darias formato a un string para 
# poder generar el string "El saldo de la cuenta 
# 32673 es $100.25"?
print("1El saldo de la cuenta {} es ${:.2f}".format(nro_cuenta, saldo))
#print("4El saldo de la cuenta {:d} es ${}".format(nro_cuenta, saldo))
print("2El saldo de la cuenta {:s} es ${:.2f}".format(nro_cuenta, saldo))
print("3El saldo de la cuenta {} es ${}".format(nro_cuenta, saldo))



