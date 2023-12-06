nip = '131951928'


def validate_nip(nip):
    weights = [6,5,7,2,3,4,5,6,7]
    # sprawdzamy czy ma 10 znaków
    # czy wszystkie znaki są cyframi 

    if len(nip) != 10:
        return False
    if not nip.isdigit():
        return False

    suma = 0
    for i in range(9):
        suma += int(nip[i]) * weights[i]


    if suma%11 != nip[9]:
        return False
    return True

if validate_nip('7819248198'):
    print("Nip is git gut")
else:
    print("Nip NOT GUT")