num = input("Anna luku: ")
array = []

while num != "":
    num0 = int(num)
    array.append(num0)
    num = input("Anna luku: ")

array.sort(reverse=True)

print(array[0:5])