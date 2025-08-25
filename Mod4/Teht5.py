otunnus = "python"
osalasana = "rules"
yritykset = 0

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

while tunnus != otunnus or salasana != osalasana:
    print("Väärä käyttäjätunnus tai salasana")
    yritykset += 1

    if yritykset == 5:
        break

    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")


if yritykset == 5:
    print("Pääsy evätty")
else:
    print("Tervetuloa")