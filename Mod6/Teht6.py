def pizzahinta(halkaisija, hinta):
    nelimetrihinta = hinta / ((halkaisija / 2) ** 2 * 3.14) * 10000
    nelihinta = round(nelimetrihinta, 2)
    return nelihinta

halkaisija = float(input("Anna pizzan halkaisija (cm): "))
hinta = float(input("Anna pizzan hinta (euroa): "))
nelihinta1 = pizzahinta(halkaisija, hinta)
print("Pizzan neliöhinta on " + str(nelihinta1) + " euroa")

halkaisija = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta = float(input("Anna toisen pizzan hinta (euroa): "))
nelihinta2 = pizzahinta(halkaisija, hinta)
print("Toisen pizzan neliöhinta on " + str(nelihinta2) + " euroa")

if nelihinta1 < nelihinta2:
    print("Ensimmäinen pizza on edullisempi.")
elif nelihinta2 < nelihinta1:
    print("Toinen pizza on edullisempi.")