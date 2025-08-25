import random

pisteet = int(input("Anna pisteiden määrä: "))
num = 0
ympPisteet = 0

while num < pisteet:
    num+=1

    rndx = random.uniform(-1,1)
    rndy = random.uniform(-1,1)

    if (rndx**2 + rndy**2) < 1:
        ympPisteet += 1

print("π arvio: " + str(4*ympPisteet/pisteet))