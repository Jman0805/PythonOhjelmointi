import random

num = int(input("Arpakuutioiden lukumäärä: "))
summa = 0

for i in range(num):
    rnd = random.randint(1,6)
    summa += rnd
    print(rnd)

print("Arvottujen silmälukujen summa: " + str(summa))