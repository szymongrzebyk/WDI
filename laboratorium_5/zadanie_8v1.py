def dzielnik(number, start, end, suma):
    if number >= suma:
        for index in range(start, end):
            if number % index == 0:
                # print(i)
                suma += index
                if index != (number / index):
                    suma += int(number / index)
                if not (index - (number / index) == 0 or (number / index) - index == 1):
                    # print("Kolejne wywołanie.")
                    suma = dzielnik(number, index + 1, int(number / (index + 1)), suma)
                    break
    return suma


# liczba = int(input("Wpisz liczbę, którą chcesz sprawdzić: "))
wynik = 1

for i in range(2, 1000000, 2):  # Nie znaleziono dotąd nieparzystej liczby doskonałej
    if i % 10000 == 0:
        print("Sprawdzam", i)
    if i == dzielnik(i, 2, int(i/2), wynik):
        print(i)
