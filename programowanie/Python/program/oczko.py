import random
lista_kart = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4]

def losuj_karte() -> int:
    dlugosc_listy = len(lista_kart)
    ostatni_index = dlugosc_listy - 1
    randomowy_indeks = random.randint(0, ostatni_index)
    wylosowana_karta =  lista_kart[randomowy_indeks]
    return wylosowana_karta

def losuj_karte_dla_gracza(gracz):
    wylosowana_karta = losuj_karte()
    gracz["wynik"] += wylosowana_karta
    print(f"Gracz {gracz['numer']} wylosował kartę {wylosowana_karta} wynik: {gracz['wynik']}")

gracze = []

grajacy_gracze = int(input("ile jest graczy? "))
for index in range(grajacy_gracze):
    gracze.append({
        "numer": index + 1,
        "wynik": 0,
        "gra": True
    })

for gracz in gracze:
    losuj_karte_dla_gracza(gracz)

def rozgrywka(gracz):
    global grajacy_gracze
    if gracz["gra"]:
        decyzja = input(f"Gracz{gracz['numer']}: Twoj wynik to: {gracz['wynik']}, Czy chcesz wylosować kartę? ")
        if decyzja == "T":
          losuj_karte_dla_gracza(gracz)
          if gracz['wynik'] > 21:
              gracz["gra"] = False
              gracz['wynik'] = 0
              grajacy_gracze = grajacy_gracze - 1 
              print(f"gracz {gracz['numer']} przegrał {grajacy_gracze}")
        else:
              gracz["gra"] = False
              grajacy_gracze = grajacy_gracze - 1

while grajacy_gracze:
    for gracz in gracze:
        rozgrywka(gracz)

winner = None

for gracz in gracze:
    if winner == None and gracz['wynik'] > 0:
        winner = gracz
    if winner != None and gracz['wynik'] > winner['wynik']:
        winner = gracz

if winner == None:
    print("Kasyno jest Winnerem")
else:
    print(f"Winnerem jest {winner}")





