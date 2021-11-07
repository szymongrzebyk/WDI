def dzielnik(number, start, end, suma):
    for i in range(start, end):
        if number % i == 0:
            # print(i)
            suma += i
            if i != (number / i):
                suma += int(number / i)
            if not (i - (number/i) == 0 or (number/i) - i == 1):
                # print("Kolejne wywołanie.")
                suma = dzielnik(number, i + 1, int(number / (i + 1)), suma)
                break
    return suma


liczba = int(input("Wpisz liczbę, którą chcesz sprawdzić: "))
wynik = 1

if liczba == dzielnik(liczba, 2, int(liczba/2), wynik):
    print(liczba)