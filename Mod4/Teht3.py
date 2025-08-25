lukuS = input("Anna luku: ")

luku = int(lukuS)

pienin = luku
suurin = luku

while lukuS != "":
    luku = int(lukuS)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
    lukuS = input("Anna luku: ")

print("Pienin luku: " + str(pienin))
print("Suurin luku: " + str(suurin))