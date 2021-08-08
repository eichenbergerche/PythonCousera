
votos = [["Alfredo", 20], ["Marcela", 40], ["Ignacio", 30], ["Loreto", 10]]


def ganador(votos):
    mayor = votos[0]
    for cand in votos:
        if cand[1] > mayor[1]:
            mayor = cand
    return mayor[0]
print(ganador(votos))

mayoria = ganador(votos)
