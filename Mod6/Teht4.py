def summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista = []

num = int(input("Anna luku: "))

while num != 0:
    lista.append(num)
    num = int(input("Anna luku: "))

print("Lukujen summa: " + str(summa(lista)))