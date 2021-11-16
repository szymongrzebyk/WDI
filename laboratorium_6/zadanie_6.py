# Na potrzeby kodu termin special oznacza, że liczba jest dwu-trzy-piątkowa
def correctInput(input):
    if input.isdigit():
        return True
    else:
        print("Musisz podać liczbę całkowitą.")
        return False


def isSpecial(number):
    if number % 5 == 0:
        new = number/5
        return isSpecial(new)
    elif number % 3 == 0:
        new = number / 3
        return isSpecial(new)
    elif number % 2 == 0:
        new = number / 2
        return isSpecial(new)
    elif number == 1:
        return True
    else:
        return False


zakres = 1
specialAmount = 0
correctType = False
while not correctType:
    zakres = input("Podaj do jakiej liczby włącznie chcesz policzyć lilczby dwu-trzy-piątkowe:")
    correctType = correctInput(zakres)
    if correctType:
        zakres = int(zakres)
for i in range(1, zakres + 1):
    if isSpecial(i):
        specialAmount += 1
print("W podanym przedziale jest", specialAmount, "liczby dwu-trzy-piątkowych.")