import random

lukuR = random.randint(1,11)

luku = 0

while luku != lukuR:
    luku = int(input("Arvaa luku väliltä 1-10: "))

    if luku < lukuR:
        print("Liian pieni arvaus")
    elif luku > lukuR:
        print("Liian suuri arvaus")
    else:
        print("Oikein")