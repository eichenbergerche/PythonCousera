secc_compra = 0
secc_venta = 0
secc_publicidad = 0
edad_emp = 0
mayor_50 = 0
empleados = 0
sueldo = 0
seccion = 0
while seccion != "fin":
    seccion = str(input("ingrese la seccion del empleado (c - seccion compra | v - seccion venta | p - seccion publicidad): "))
    if seccion != "c" and seccion != "v" and seccion != "p" and seccion != "v":
        print("---ingrese por favor el seccion correspondinte (c - seccion compra | v - seccion venta | p - seccion publicidad)---")
    elif seccion == "c":
        secc_compra += 1
        edad_emp = int(input("ingrese la edad del empleado: "))
        if edad_emp >= 50:
            mayor_50 += 1        
        sueldo = sueldo + float(input("ingrese el sueldo del empleado en la seccion compra: "))
        empleados += 1
    elif seccion == "v":
        secc_venta += 1
        edad_emp = int(input("ingrese la edad del empleado: "))
        if edad_emp >= 50:
            mayor_50 += 1   
        sueldo = sueldo + float(input("ingrese el sueldo del empleado en la seccion venta: "))
        empleados += 1
    elif seccion == "p":
        secc_publicidad += 1
        edad_emp = int(input("ingrese la edad del empleado: "))
        if edad_emp >= 50:
            mayor_50 += 1   
        sueldo = sueldo + float(input("ingrese el sueldo del empleado en la seccion publicidad: "))
        empleados += 1
sueldo_prom = sueldo / empleados
print("el total de empleados es: ", empleados)
print("el total de empleados en la seccion compra es:", secc_compra)
print("el total de empleados en la seccion publicidad es:", secc_publicidad)
print("el total de empleados en la seccion venta es:", secc_venta)
print("el total de empleados mayores a 50 años es:", mayor_50)
print("el sueldo promedio es:", str(round(sueldo_prom, 2)))