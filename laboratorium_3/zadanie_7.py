# Jako, że w danych  zadania nie ma sprecyzowanego,
# czy przedział  ma być domknięty zastosowałem przeział domknięty obustronnie

beginning = int(input("Proszę podać początek przedziału "))
ending = int(input("Proszę podać koniec przedziału "))
zakres = float(ending - beginning + 1)
if zakres > 20:
    if zakres % 2 == 0:
        for i in range(int(zakres/2 - 3), int(zakres/2 + 3)):
            print(i)
    elif zakres % 2 == 1:
        for i in range(int((zakres + 1)/2 - 3), int((zakres + 1)/2 - 1)):
            print(i)
        for i in range(int((zakres + 1)/2 + 1), int((zakres + 1)/2 + 3)):
            print(i)
else:
    for i in  range(beginning, ending + 1):
        print(i)
