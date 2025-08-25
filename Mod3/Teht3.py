sukupuoli = input("Sukupuoli (m/f): ")

if sukupuoli == "m":
    hemoglobiini = float(input("Hemoglobiiniarvo (g/l): "))
    if hemoglobiini < 134:
        print("Alhainen hemoglobiinitaso")
    elif hemoglobiini > 195:
        print("Korkea hemoglobiinitaso")
    else:
        print("Normaali hemoglobiinitaso")
elif sukupuoli == "f":
    hemoglobiini = float(input("Hemoglobiiniarvo (g/l): "))
    if hemoglobiini < 117:
        print("Alhainen hemoglobiinitaso")
    elif hemoglobiini > 175:
        print("Korkea hemoglobiinitaso")
    else:
        print("Normaali hemoglobiinitaso")
else:
    print("Virheellinen sukupuoli")