print("Colocar la cantidad de asistencia")
asistencia = int(input())
print("Colocar la cantidad total de asistencias")
total_asis = int(input())
porciento_asis = asistencia / total_asis * 100
print("El porcentaje de asistencia es: " + str(round(porciento_asis, 2)), "%")