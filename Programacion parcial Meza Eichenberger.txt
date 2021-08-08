emp_textil = 0
emp_construccion = 0
emp_servicios = 0
empleados = 0
sueldo = 0
seccion = 0
print("-------------------Examen Parcial de Programación---------------------")
while seccion != "fin":
    seccion = str(input("ingrese el seccieon del empleado (t - textil | c - construccion | s - servicios): "))
    if seccion != "t" and seccion != "c" and seccion != "s":
        print("ingrese por favor el seccion correspondinte (t - textil | c - construccion | s - servicios)")
    elif seccion == "t":
        emp_textil += 1
        sueldo = sueldo + float(input("ingrese el sueldo del empleado del seccion textil: $"))
        empleados += 1
    elif seccion == "c":
        emp_construccion += 1
        sueldo = sueldo + float(input("ingrese el sueldo del empleado del seccion construccion: $"))
        empleados += 1
    elif seccion == "s":
        emp_servicios += 1
        sueldo = sueldo + float(input("ingrese el sueldo del empleado del seccion servicios: $"))
        empleados += 1
sueldoprom = sueldo / empleados
print("--------------------Examen Parcial de Programación--------------------")
print("el total de empleados en la empresa es: ", empleados)
print("el total de empleados en la seccion de textil es:", emp_textil)
print("el total de empleados en la seccion de servicios es:", emp_servicios)
print("el total de empleados en la seccion de construccion es:", emp_construccion)
print("el sueldo promedio es: $", str(round(sueldoprom, 2)))
print("--------------------Meza Eichenberger Charles Henry--------------------")