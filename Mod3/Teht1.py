pituus = float(input("Kuhan pituus: "))

if pituus < 37:
    alimitta = 37 - pituus
    print("Kuha on " + str(alimitta) + " cm verran alamittainen, laske se takaisin veteen.")
else:
    print("Kuha on tarpeeksi iso")