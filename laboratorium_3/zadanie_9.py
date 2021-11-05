saldo = 0
wplata = 0
wyplata = 0
choice = 0
correctPin = False
correctAmount = False
print("Jest to twoje pierwsze użycie tego programu. "
      "Musisz ustawić swój kod PIN, którym będziesz autoryzował wszystkie późniejsze operacje.")
while not correctPin:
    pin = int(input("Podaj kod PIN: "))
    pinCheck = int(input("Podaj ponownie kod PIN: "))
    if pin < 1000 or pin > 9999:
        print("PIN musi być 4-cyfrowy i nie może zaczynać się od zera. Podaj  ponownie.")
    elif pin != pinCheck:
        print("Kody PIN nie są identyczne. Podaj ponownie.")
    else:
        correctPin = True
correctPin = False
print("Witaj. ", end = '')
while choice != 4:
    correctPin = False
    correctAmount = False
    print("Co chcesz zrobić?")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie salda")
    print("4. Wyjście")
    choice = int(input("Wybór: "))
    if choice == 1:
        while not correctPin:
            pinCheck = int(input("Podaj PIN: "))
            if pin != pinCheck:
                print("PIN niewłaściwy.")
            else:
                correctPin = True
        wplata = int(input("Podaj kwotę wpłaty: "))
        saldo += wplata
    elif choice == 2:
        while not correctPin:
            pinCheck = int(input("Podaj PIN: "))
            if pin != pinCheck:
                print("PIN niewłaściwy.")
            else:
                correctPin = True
        while not correctAmount:
            wyplata = int(input("Podaj kwotę wypłaty: "))
            if wyplata > saldo:
                print("Nie masz tylu środków.")
            else:
                correctAmount = True
        saldo -= wyplata
    elif choice == 3:
        while not correctPin:
            pinCheck = int(input("Podaj PIN: "))
            if pin != pinCheck:
                print("PIN niewłaściwy.")
            else:
                correctPin = True
        print("Twoje saldo wynosi:", saldo)
    elif choice == 4:
        break
    else:
        print("Podaj liczbę z odpowiedniego przedziału")