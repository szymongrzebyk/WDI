num1 = 0
num2 = 0
# Użytkownik wpisuje liczby,
# jeśli są równe zero  musi wpisać drugi raz
while num1 == 0 or num2 == 0:
    # Wczytywanie liczb
    num1 = int(input("Podaj pierwszą liczbę, różną od zera "))
    num2 = int(input("Podaj drugą liczbę, różną od zera "))
# Sprawdzenie warunku z 6.d i 6.e
if num1 < 0 and num2 < 0:
    print("Podane liczby są ujemne.")
    exit()
elif num1 < 0 and num2 >= 0:
    print("Zostanie użyta wartość bezwzględna z liczby", num1)
    num1 = abs(num1)
elif num1 >= 0 and num2 < 0:
    print("Zostanie użyta wartość bezwzględna z liczby", num2)
    num2 = abs(num2)

# Liczenie wartości
suma = num1 + num2
roznica = num1 - num2
iloczyn = num1 * num2
iloraz = num1/num2
num1Sqr = num1**2
num2Sqr = num2**2
num1Root = num1**(1/2)
num2Root = num2**(1/2)

# 6.a
print("Wynik dodawania liczb", num1, "i", num2, "to", suma)
print("Wynik odejmowania liczb", num1, "i", num2, "to", roznica)
print("Wynik mnożenia liczb", num1, "i", num2, "to", iloczyn)
print("Wynik dzielenia liczb", num1, "i", num2, "to", iloraz)
print("Kwadrat liczby", num1, "to", num1Sqr)
print("Kwadrat liczby", num2, "to", num2Sqr)
print("Pierwsiastek kwadratowy liczby", num1, "to", num1Root)
print("Pierwsiastek kwadratowy liczby", num2, "to", num2Root)

# 6.f
if iloczyn == 10:
    print("Yay!")
