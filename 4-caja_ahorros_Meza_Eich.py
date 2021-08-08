caja_ahorros = 50000
print ("Su caja de ahorros cuenta actualmente con $"+ str(caja_ahorros))
print ("Ingrese monto a retirar")
retirar = int(input())
saldo = caja_ahorros - retirar
if saldo == 0:
    print ("Usted no tiene saldo en la caja de ahorros")
elif saldo <= 0:
    print ("Usted no cuenta con ese saldo, por favor intente nuevamente, su saldo actual es $"+ str(caja_ahorros))
else:
    print ("Su saldo actual es de $"+ str(saldo))