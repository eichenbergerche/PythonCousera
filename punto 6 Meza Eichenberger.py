emp_armado = 0
emp_empaquetado = 0
emp_ventas = 0
empleados = 0
sueldo = 0
area = 0
while area != "fin":
    area = str(input("ingrese el area del empleado (a - armado | e - empaquetado | v - ventas): "))
    if area != "a" and area != "e" and area != "v":
        print("ingrese por favor el area correspondinte (a - armado | e - empaquetado | v - ventas)")
    elif area == "a":
        emp_armado += 1
        sueldo = sueldo + float(input("ingrese el sueldo del empleado del Area armado: $"))
        empleados += 1
    elif area == "e":
        emp_empaquetado += 1
        sueldo = sueldo + float(input("ingrese el sueldo del empleado del Area empaquetado: $"))
        empleados += 1
    elif area == "v":
        emp_ventas += 1
        sueldo = sueldo + float(input("ingrese el sueldo del empleado del Area ventas: $"))
        empleados += 1
sueldoprom = sueldo / empleados
print("el total de empleados en la empresa es: ", empleados)
print("el total de empleados en el area de armado es:", emp_armado)
print("el total de empleados en el area de ventas es:", emp_ventas)
print("el total de empleados en el area de empaquetado es:", emp_empaquetado)
print("el sueldo promedio es: $", str(round(sueldoprom, 2)))
