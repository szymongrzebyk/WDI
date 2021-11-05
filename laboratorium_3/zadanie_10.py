from random import randint
choice = 'T'

print("Proszę podać 2 liczby, a następnie znak operacji, wedle następującej legendy:")
print("Dodawanie: +")
print("Odejmowanie: -")
print("Mnożenie: *")
print("Dzielenie: /")
print("Potęgowanie: **")
print("Pierwiastkowanie: ^")
print("Losowanie z zakresu: x")
while choice == 'T':
    num1 = int(input("Podaj pierwszą liczbę: "))
    num2 = int(input("Podaj drugą liczbę: "))
    znak = input("Podaj znak operacji: ")
    if znak == '+':
        print(num1, "+", num2, "=", num1 + num2)
    elif znak == '-':
        print(num1, "-", num2, "=", num1 - num2)
    elif znak == '*':
        print(num1, "*", num2, "=", num1*num2)
    elif znak == '/':
        print(num1, "/", num2, "=", num1/num2)
    elif znak == '**':
        print(num1, "**", num2, "=", num1**num2)
    elif znak == '^':
        print(num1, "^", num2, "=", num1**(1/num2))
    elif znak == 'x':
        print("Losowa liczba z przedziału <", num1, ",", num2, "> to", randint(num1, num2))
    choice = 0
    while not (choice == 'T' or choice == 'N'):
        choice = input("Czy chcesz wprowadzić nowe dane? (T/N)  ")
        if not (choice == 'T' or choice == 'N'):
            print("Wpisz znak T lub N!")
