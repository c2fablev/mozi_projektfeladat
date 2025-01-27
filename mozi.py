import random
arak = [2500, 2100, 1300, 0]

def feltoltes(lista:list):
    for i in range(15):
        kislista = []
        for j in range(10):
            kislista.append(random.choice(arak))
        kislista.append("|")
        for j in range(10):
            kislista.append(random.choice(arak))
            print(len(kislista))
        lista.append(kislista)
    return lista
