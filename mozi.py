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
        lista.append(kislista)
    return lista

def jegyVasarlas(szam:int):
    while szam <2 or szam >5:
        print("Hány jegyet szeretne vásárolni? (2-5)", end="")
        szam = int(input())
    return szam

def helykereses(moziTerem:list, helyekSzama:int):
    egybefuggo = 0
    i = 1
    for sor in moziTerem:
        egybefuggo = 0
        for hely in sor:
            if hely == 0:
                egybefuggo += 1
            else:
                egybefuggo = 0
            if egybefuggo >= helyekSzama:
                return i
        i += 1

moziterem = []
feltoltes(moziterem)
for sor in moziterem:
    print(sor)
jegyek = jegyVasarlas(jegyek)
if helykereses(moziterem, jegyek) != None:
    print(helykereses(moziterem, jegyek))
else:
    print("nincs hely! :(")