# Napisz funkcję, która obliczy sumę cyfr liczby całkowitej.

def suma(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(suma((8, 2, 3, 0, 7)))

# Sposob drugi

def dodaj(a,b):
    wynik = a + b
    return wynik
suma = dodaj(3,6)
print(suma)

# Sposób trzeci

def suma(liczba):
    return sum(int(cyfra) for cyfra in str(liczba))
print(suma(123))


# Sposób czwarty
def SumNumber(digit:str) ->int:
    total = 0
    for digit in digit:
        total += int(digit)
    return total

try:
    number = input('Enter a number: ')
    if number.isdigit():
        result = SumNumber(number)
        print(f"suma cyfr liczby {number} wynosi:{result}")
    else:
        print("Plesae entert only digits")
except ValueError:
    print("Invalid input")