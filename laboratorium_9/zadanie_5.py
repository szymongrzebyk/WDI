# Getting size and creating array
while True:
    try:
        N = int(input("Podaj rozmiar tablicy:"))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("Musisz podać dodatnią liczbę całkowitą!")
array = []
for i in range(N):
    array.append([0] * N)

# Putting N^2 elements of Fibonacci string into one list
fibonacci = [0, 1]
fibonacciPointer = 0
for i in range(2, N**2):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
lastElementString = str(fibonacci[-1])
lastElementLength = len(lastElementString)


# Functions used in filling array
def fillRight(x, y, length):
    global array
    for index in range(length):
        array[x][y + index] = fibonacci[fibonacciPointer + index]


def fillDown(x, y, length):
    global array
    for index in range(length):
        array[x + index][y] = fibonacci[fibonacciPointer + index]


def fillLeft(x, y, length):
    global array
    for index in range(length):
        array[x][y - index] = fibonacci[fibonacciPointer + index]


def fillUp(x, y, length):
    global array
    for index in range(length):
        array[x - index][y] = fibonacci[fibonacciPointer + index]


def square(start, sizer):
    global fibonacciPointer
    length = N - sizer
    end = start + length
    if length == 0:
        array[start][start] = fibonacci[fibonacciPointer]
    else:
        fillRight(start, start, length)
        fibonacciPointer += length

        fillDown(start, end, length)
        fibonacciPointer += length

        fillLeft(end, end, length)
        fibonacciPointer += length

        fillUp(end, start, length)
        fibonacciPointer += length


# Printing array, should be formatted but it's not
def printArray(table):
    for row in range(N):
        print(array[row])
        # for column in range(N):
        # print('{num:width}'.format(num=array[row][column], width=int(lastElementLength)))
        # '{num:0:{width}}'.format(num=array[row][column], width=lastElementLength)
        # print("%d*lastElementLength", array[row][column])


# Executing square function certain amount of times to fill array
array[0][0] = 0
for step in range(1, N+1, 2):
    position = int((step - 1) / 2)
    square(position, step)
print(fibonacci)
printArray(array)
