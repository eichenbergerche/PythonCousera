print("escribi pe un numerito entre 0 y 100")
numero=int(input())
print("tu numerito e:", numero)
if(numero<100):
    print("tu numero co e mas bajito que 100")
    Nfaltan=0
    while numero<100:
        for numero in range(numero, 100,1):
            numero+=1
            Nfaltan+=1
    print("faltan", Nfaltan,"numero/s para llegar a 100 mi rey")
else:
    print("no seas wampa no ves que tu numero es mayor que 100 gil")
print("nos ve mi tegen")