from random import seed
from random import randint
size = int(input("Wpisz rozmiar choinki "))
# size = 10
ball = 0
# seed(1)
# Budowanie gwiazdy
for index in range(size - 1):
    print(" ", end = '')
print("X")
# Budowanie choinki
for index in range(2, size + 1):
    ball = randint(1, 100)
    for j in range(size - index):
        print(" ", end = '')
    for j in range((index*2) - 1):
        if (j + ball) % (10 + j) == 0:
            print("o", end = '')
        else:
            print("*", end = '')
    print("")
# Budowanie pnia
for index in range(size - 1):
    print(" ", end = '')
print("U")