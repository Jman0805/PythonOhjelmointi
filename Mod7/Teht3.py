lentoasemat = {
    "EFHK": "Helsinki-Vantaa",
    "EFJY": "Jyväskylä",
    "EFTU": "Turku",}

komento = input("Valitse komento (lisää, hae, lopeta): ")

while komento != "lopeta":
    if komento == "lisää":
        tunnus = input("Anna lentokentän ICAO-koodi: ")
        nimi = input("Anna lentokentän nimi: ")
        lentoasemat[tunnus] = nimi
    elif komento == "hae":
        tunnus = input("Anna lentokentän ICAO-koodi: ")
        if tunnus in lentoasemat:
            print(f"Lentokenttä {tunnus} on {lentoasemat[tunnus]}.")
        else:
            print("Lentokenttää ei löydy.")
    else:
        print("Virheellinen komento.")
    komento = input("Valitse komento (lisää, hae, lopeta): ")