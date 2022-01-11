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


while True:
    try:
        first = int(input("Podaj pierwszą liczbę:"))
        if first <= 0:
            raise ValueError
        break
    except ValueError:
        print("Musisz podać dodatnią liczbę całkowitą!")

while True:
    try:
        second = int(input("Podaj drugą liczbę:"))
        if second <= 0:
            raise ValueError
        break
    except ValueError:
        print("Musisz podać dodatnią liczbę całkowitą!")

organized = organize(first, second)  # getting tuple, bigger than lesser
print("NWD liczb", organized, "równa się", euklides(organized[0], organized[1]))
