def litramuutos(gallona):
    return gallona * 3.785

gallonat = float(input("Anna gallonamäärä: "))

while gallonat > 0:
    print(str(litramuutos(gallonat)) + " litraa")
    gallonat = float(input("Anna gallonamäärä: "))
