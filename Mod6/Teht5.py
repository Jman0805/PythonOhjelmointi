def pariton(luvut):
    uLista = []
    for luku in luvut:
        if luku % 2 != 0:
            uLista.append(luku)
    return uLista

lista = []

num = int(input("Anna luku: "))

while num != 0:
    lista.append(num)
    num = int(input("Anna luku: "))

print("Alkuperäinen lista: " + str(lista))
print("Pariton lista: " + str(pariton(lista)))