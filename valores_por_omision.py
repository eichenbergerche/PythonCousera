def pedir_confirmacion(prompt, reintentos=4, recordatorio="Por favor intente nuevamente"):
    while True:
        ok= input(prompt)
        if ok in ("s", "S", "si", "Si", "SI"):
            return True
        if ok in ("n", "no", "No", "NO"):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError("respuesta de usuario invalida")
        print(recordatorio)
