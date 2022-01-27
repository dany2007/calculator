import random

list = []
operatii = ["+", "-", "*", "/"]
for i in range(100):
    element = [random.randint(0, 100), random.choice(operatii), random.randint(0, 100) ,"\n"]
    list.append(" ".join([str(elem) for elem in element]))

with open("input.txt", "w+") as file:
    for elem in list:
        file.writelines(str(elem))
