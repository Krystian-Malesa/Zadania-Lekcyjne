

def validate_pesel(pesel: str) -> bool:
    weights = [1,3,7,9,1,3,7,9,1,3]
    # sprawdzamy czy ma 10 znaków
    # czy wszystkie znaki są cyframi 

    if len(pesel) != 11:
        return False
    if not pesel.isdigit():
        return False

    suma = 0
    for i in range(10):
        suma += int(pesel[i]) * weights[i]

    ostatnia_cyfra_sumy = int(str(suma)[-1]) # 17 -> 7
    if ostatnia_cyfra_sumy == 0:
        if ostatnia_cyfra_sumy == int(pesel[-1]):
            return True
        else:
            return False
    if 10 - ostatnia_cyfra_sumy == int(pesel[-1]):
        return True
    else:
        return False

if validate_pesel('03261205018'):
    print("pesel is git gut")
else:
    print("pesel NOT GUT")