luotiPaino = 13.3
naulaPaino = luotiPaino * 32
leiviskaPaino = naulaPaino * 20

leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

yhteisPaino = (leiviskat * leiviskaPaino) + (naulat * naulaPaino) + (luodit * luotiPaino)
kilot = int(yhteisPaino // 1000)
grammat = yhteisPaino - (kilot * 1000)

print("Massa nykymittojen mukaan: \n" + str(kilot) + " kilogrammaa ja " + str(round(grammat,2)) + " grammaa.")