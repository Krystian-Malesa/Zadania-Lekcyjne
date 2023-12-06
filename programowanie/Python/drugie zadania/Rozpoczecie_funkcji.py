# Zadanie 1:
# Napisz funkcje powitanie, która nie przyjmuje żadnych argumentów i wypisuje "Witaj w swiecie Pythona!"

# def powitanie ():
#     print("Witaj w swiecie Pythona!")


# Zadanie 2:
# Zmodyfikuj funkcje powitanie tak, aby przyjmowała jeden argument imie i wypisywała personalizowane powitanie.

# def powitanie(imie):
#     print(f"Witaj, {imie}, w świecie Pythona!")

# powitanie("Anna")

# Zadanie 5:
# Napisz funkcję max_min, która przyjmuje trzy argumenty i zwraca wartość maksymalną oraz minimalną.

# dane = [1,2,3,4,5,6]

# def max_min(dane):
#     return max(dane), min(dane)

# print(max_min(dane))

# Zadnie 6:
# Stwórz funkcję dlugosc_ciagu, która przyjmuje string i zwaraca liczbę znaków w tym stringu.

from datetime import datetime


def dlugosc_ciagu(ciag):
    return len(ciag)
print(dlugosc_ciagu("Python"))

# Zadanie 7:
# Napisz funkcje silnia, któa oblicza silnię danej liczby.

def silnia(n):
    if n==0:
        return 1
    else:
        return n * silnia(n-1)

s = silnia(10)
print(s)


# Zadanie 12:
# Napisz funckję z adnotacją typów, która sumuje dwie liczby całkowite.


# def suma (a: int,b: int):
#     return a + b
# print(suma(10,5))

print(datetime.strptime("08 05 2015","%m %d %Y").strftime("%A").upper())


    