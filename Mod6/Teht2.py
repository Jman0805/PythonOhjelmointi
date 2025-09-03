import random

def arpa(tahkot):

    return random.randint(1,tahkot)

max = int(input("Maksimitahkot: "))

while True:
    num = arpa(max)
    print(num)
    if num == max:
        break