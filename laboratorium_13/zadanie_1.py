def euklides(bigger, lesser):   # if those numbers are equal their order doesn't matter
    wynik = bigger % lesser
    print(bigger, "=", int((bigger - wynik)/lesser), "*", lesser, "+", wynik)
    if wynik == 0:
        return lesser
    else:
        return euklides(lesser, wynik)


def organize(num1, num2):
    if num1 >= num2:
        return num1, num2
    if num2 > num1:
        return num2, num1


def getNumber():
    while True:
        try:
            number = 10
            # number = int(input("Podaj liczbę:"))
            if number <= 0:
                raise ValueError
            break
        except ValueError:
            print("Musisz podać dodatnią liczbę całkowitą!")
    return number

first = getNumber()
second = getNumber()
organized = organize(first, second)  # getting tuple, bigger than lesser
print("NWD liczb", organized, "równa się", euklides(organized[0], organized[1]))
