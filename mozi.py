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
        try:
            szam = int(input())
        except:
            print("Egész zámot adjon meg!")
            return jegyVasarlas(szam)
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

def bevetel(moziTerem:list):
    szumma = 0
    for sor in moziTerem:
        for hely in sor:
            if hely != "|":
                szumma += hely
    return szumma

def kihasznaltsag(moziTerem:list):
    darab = 0
    for sor in moziTerem:
        for hely in sor:
            if hely != "|":
                if hely != 0:
                    darab += 1
    kihasznalt = (darab / 300) * 100
    return int(kihasznalt * 100)/100

def teljesAruJegyek(moziTerem:list):
    teljesAruJegy = 0
    for sor in moziTerem:
        for hely in sor:
            if hely == 2500:
                teljesAruJegy += 1
    return teljesAruJegy

moziterem = []
feltoltes(moziterem)
jegyek = jegyVasarlas(jegyek)
if helykereses(moziterem, jegyek) != None:
    print(f"{helykereses(moziterem, jegyek)}. sorban van hely!")
else:
    print("Nincs hely! :(")
print(f"Az összes bevétel: {bevetel(moziterem)} Ft")
print("A kihasználtság:", kihasznaltsag(moziterem), "%")
print(f"Teljes árú jegyek száma: {teljesAruJegyek(moziterem)} db")