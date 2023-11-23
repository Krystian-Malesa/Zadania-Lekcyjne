# Pierwszy program:
# Napisz program, który wypisze na ekranie "Hello, World!"
##### print("Hello, World!")

# Wypisywanie danych na ekran:
# Poproś użytkownika o podanie swojego imienia i wypisz je na ekranie w zdaniu np. "Witaj Jan!"

imie = input("Podaj swoje imie: ")
nazwisko = "Kowalski"
print("Witaj, " + imie + "!")
print(f"Witaj, {imie} !")
print("Witaj, {}!".format(imie))
print("Witaj, {0} {1}, {1} {0}!".format(imie,nazwisko))