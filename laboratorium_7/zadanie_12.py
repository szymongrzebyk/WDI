class OperationCharacterError(Exception):
    pass


def changeIntoList(userInput):
    listedInput = []
    while userInput > 0:
        digit = userInput % 10
        listedInput.insert(0, digit)
        userInput = int((userInput - (userInput % 10)) / 10)
    return listedInput


def adjustLength(list1, list2):
    if len(list1) >= len(list2):
        return list1
    else:
        for i in range(len(list2) - len(list1)):
            list1.insert(0, 0)
        return list1


def addition(element1, element2):
    element1 = adjustLength(element1, element2)
    element2 = adjustLength(element2, element1)
    result = []
    carriedValue = 0
    for index in range(len(element1)):
        sum = element1[-(index + 1)] + element2[-(index + 1)]
        digit = int(sum % 10 + carriedValue)
        result.insert(0, digit)
        carriedValue = int((sum - (sum % 10)) / 10)
    return result


def subtraction(minuend, subtrahend):  #   minuend znaczy odjemna, subtrahend znaczy odjemnik
    subtrahend = adjustLength(subtrahend, minuend)
    result = []
    borrowedValue = 0
    for index in range(len(minuend)):
        difference = int((minuend[-(index + 1)] - subtrahend[-(index + 1)]) - (borrowedValue / 10))
        if minuend[-(index + 1)] < subtrahend[-(index + 1)]:
            borrowedValue = 10
        else:
            borrowedValue = 0
        digit = int((difference + borrowedValue) % 10)
        result.insert(0, digit)
    return result


number1 = int(input("Proszę podać pierwszą liczbę: "))
number2 = int(input("Proszę podać drugą liczbę: "))
action = input("Proszę podać znak dxziałania (+ lub -): ")
listedNumber1 = changeIntoList(number1)
listedNumber2 = changeIntoList(number2)
print(listedNumber1)
print(listedNumber2)
try:
    if action == '+':
        addedNumbers = addition(listedNumber1, listedNumber2)
        print(addedNumbers)
    elif action == '-':
        if len(listedNumber1) > len(listedNumber2):
            subtractedNumbers = subtraction(listedNumber1, listedNumber2)
        elif len(listedNumber1) < len(listedNumber2):
            subtractedNumbers = subtraction(listedNumber2, listedNumber1)
        else:
            for i in range(len(listedNumber1)):
                if listedNumber1[i] > listedNumber2[i]:
                    subtractedNumbers = subtraction(listedNumber1, listedNumber2)
                    break
                elif listedNumber1[i] < listedNumber2[i]:
                    subtractedNumbers = subtraction(listedNumber2, listedNumber1)
                    break
                elif i == (len(listedNumber1) - 1) and listedNumber1[i] == listedNumber2[i]:
                    subtractedNumbers = subtraction(listedNumber1, listedNumber2)
                    break
        print(subtractedNumbers)
    else:
        raise OperationCharacterError
except OperationCharacterError:
    print("Możliwe jest tylko działanie dodawania i odejmowania!")