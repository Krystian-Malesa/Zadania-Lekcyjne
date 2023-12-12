import json

def read_from_file(nazwa_pliku, nazwa):
    try:
        with open(nazwa_pliku,'r', encoding='utf8') as file:
            dane = json.load(file)
            dane["nazwa"]
            if nazwa == dane["nazwa"]:
                return dane
    except FileNotFoundError:
        return False


def pokaz_przepis(przepis):
    print(f"Przepis na ciasto {przepis['nazwa']}")
    for skladniki, dane in przepis['skladniki'].items():
        print(f"-{skladniki}: {dane['ilosc']} {dane['jednostka']}")


def save_to_file(nazwa_pliku,przepis):
    with open(nazwa_pliku,'w') as file:
        return json.dump(przepis, file ,indent = 4 )

def dodaj_ciasto(nazwa):

    return {"nazwa": nazwa,
            "skladniki":{}
            }



def dodaj_skladnik(ciasto, skladnik,ilosc,jednostka):
    ciasto["skladniki"][skladnik] = {
            "ilosc": ilosc,
            "jednostka" : jednostka
        }



# przepis = read_from_file("czekoladowe.json","Jabłecznik")
# pokaz_przepis(przepis)

ciasto = dodaj_ciasto("Czekoladowe")
dodaj_skladnik(ciasto, "Czekolada","1","sztuk")
dodaj_skladnik(ciasto, "Mleko w proszku","1","sztuk")
save_to_file("czkoladowe", ciasto)