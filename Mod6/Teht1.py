import random

def arpa():
    return random.randint(1,6)

while True:
    num = arpa()
    print(num)
    if num == 6:
        break