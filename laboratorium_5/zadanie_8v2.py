def isPrime(number):
    for dzielnik in range(2, number - 1):
        if number % dzielnik == 0:
            return False
    return True


def makePerfect(number):
    if isPrime((2**number) - 1):
        perfect = ((2**number) - 1)*(2**(number - 1))
        return perfect
    return 0


for i in range(31):
    if isPrime(i):
        liczba = makePerfect(i)
        if liczba > 0:
            print(liczba)
