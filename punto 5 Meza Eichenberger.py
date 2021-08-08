total = 0
importe = print("-----------------gastos---------------------")
while importe != 0:
    importe = float(input("ingresar los importes de la compra: $"))
    total = total + importe
    iva = (total * 21) / 100
    iva_importe = total + iva
print("el importe mas IVA del 21% es: $",str(round(iva_importe, 2)))