imie = "Robert"
lista = ["Jan","Robert"]
if imie in lista:
    print("jest")
else:
    print("nie ma")

print("===========")
 
a = 45
a = a + 10
a +=10  
a -= 50
a **=3
a//=30
print(a)
print("===========")

wiek = False
if wiek:
  print("jesteś pełnoletni 1")
  print("kazik")

print("===========")


wiek= int(input(f"{imie} podaj swój wiek"))
if wiek >= 18:
     print("jesteś pełnoletni")
else:
    print("nie jesteś pełnoletni")

print("===========")


wiek= input("podaj swój wiek")

if wiek.isnumeric(): 
    print("sss")
else:
    wiek= input("podaj wiek jako liczę")




wiek = int(wiek)
if wiek >= 18:
    print("jesteś pełnoletni")
else:
    print("nie jesteś pełnoletni")

print()