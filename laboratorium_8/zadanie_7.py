def isPrime(number):
    for dzielnik in range(2, number - 1):
        if number % dzielnik == 0:
            return False
    return True


def dividesOnce(number, factor):
    if number % factor == 0:
        if (number / factor) % factor == 0:
            return False
    return True


def jednokrotna(liczba):
    for index in range (2, liczba):
        if isPrime(index):
            if liczba % index == 0:
                if not dividesOnce(liczba, index):
                    return False
    return True


def euklides(bigger, lesser, carry):   # if those numbers are equal their order doesn't matter
    wynik = bigger % lesser
    if wynik == 0:
        return carry
    else:
        return euklides(lesser, wynik, wynik)


def coprime(number1, number2):
    if number1 >= number2:
        if euklides(number1, number2) == 1:
            return True
        else:
            return False
    else:
        if euklides(number1, number2) == 1:
            return True
        else:
            return False


# list = [15, 45, 58, 548, 248, 5, 8, 8, 7, 5, 4, 8, 5, 858, 45, 98, 2]
# list = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
# list = [5, 5, 5, 5, 5, 8, 2, 3, 45, 7, 11, 13, 17, 19, 23, 29, 46, 8]
# list = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
list = [1, 1, 1, 32, 1, 1, 1, 1]
biggestLength = 0
longestSubstringBeginning = 0
tempSubstringEnd = 1
tempSubstringBeginning = 0
product = list[0]
while tempSubstringEnd < len(list):
    if not jednokrotna(list[tempSubstringEnd]) or not jednokrotna(list[tempSubstringBeginning]):
        if biggestLength < (tempSubstringEnd - tempSubstringBeginning):
            biggestLength = (tempSubstringEnd - tempSubstringBeginning)
            longestSubstringBeginning = tempSubstringBeginning
        if tempSubstringEnd + 1 >= len(list) or tempSubstringBeginning >= len(list):
            break
        else:
            tempSubstringBeginning = tempSubstringEnd + 1
            tempSubstringEnd = tempSubstringBeginning
            product = list[tempSubstringBeginning]
    elif not coprime(product, list[tempSubstringEnd]):
        if biggestLength < (tempSubstringEnd - tempSubstringBeginning):
            biggestLength = (tempSubstringEnd - tempSubstringBeginning)
            longestSubstringBeginning = tempSubstringBeginning
        while not tempSubstringBeginning == tempSubstringEnd:
            product /= list[tempSubstringBeginning]
            tempSubstringBeginning += 1
            if coprime(product, list[tempSubstringEnd]):
                product *= list[tempSubstringEnd]
                break
    else:
        product *= list[tempSubstringEnd]
    tempSubstringEnd += 1
print(biggestLength, longestSubstringBeginning)
