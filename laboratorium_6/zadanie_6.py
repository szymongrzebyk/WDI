# Na potrzeby kodu termin special oznacza, że liczba jest dwu-trzy-piątkowa

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
# while True:
#     try:
#         zakres = int(input("Podaj do jakiej liczby włącznie chcesz policzyć lilczby dwu-trzy-piątkowe:"))
#         break
#     except ValueError:
#         print("Musisz podać liczbę całkowitą.")
for i in range(1, zakres + 1):
    if isSpecial(i):
        specialAmount += 1
print("W podanym przedziale jest", specialAmount, "liczb dwu-trzy-piątkowych.")