import random
arak = [2500, 2100, 1300, 0]
jegyek = 6
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

def jegyVasarlas(szam:int):
    while szam <=2 or szam >=5:
        print("Hány jegyet szeretne vásárolni? (2-5)", end="")
        szam = int(input())
    return szam


