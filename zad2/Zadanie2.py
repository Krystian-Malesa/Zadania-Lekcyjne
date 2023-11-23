# Zadanie 1: Wykonywanie prostej prośby GET 

# import requests

# response = requests.get('https://www.google.com')
# print(response.status_code)
# print(response.text)


# Zadanie 2: Walidacja adresu e-mail

#- czy istnieje @
#- walidacja pustych znaków
#- user ma od 6-30 znaków
# - domena to pw.edu.pl

# email = ("abc.abc@pw.edu.pl")

# def validate_email(email):
#
#    if email.count('@') != 1 :
#        #return False 
#          raise ValueError("TO NIE JEST ADRES MAILOWY,!")
#    # podzial adres na username i domene
#    param = email.split('@')
#    if param[1] == 'pw.edu.pl':
#        True
#
#    return True

#try:
#    validate_email('jakub.chmielak@pw.edu.pl')
#except ValueError as e:
#    print(f"Komunikat błedu: {e}")


# Napisz funkcję validate_password, która sprawdza, czy hasło jest wystarczająco silnie. Założmy że silne hasło musi mieć przynajmniej 8 znaków, w tym jedną cyfrę i jedną wielką literę.

# haslo = ("maniek")
#
#
# def validate_password(haslo):
#    
#    mam_cyfre = any(char.isdigit() for char in haslo)
#    mam_duza_litera = any(char.isupper() for char in haslo)
#    is_long = len(haslo) >= 8
#    return mam_cyfre and mam_duza_litera and is_long 

# password = input("Wprowadz haslo: ")

# if validate_password(password):
#     print("Git gut haslo")


# Napisz funckję validate_username, która sprawdza, czy nazwa użytkownika skłąda się wyłaczenie z liter i cyfr oraz czy ma od 3 do 16 znaków.

#user =("kowals!@!")

#def validate_username(user):
#    is_long = len(user) <= 3 >= 16
#    only_licz_lit = user.isalnum()
#    return is_long and only_licz_lit

#if validate_username(user):
#    print("git gut uzyszkownik")


#def validate_username(username):
#    return username.isalnum() and 3 <= len(username) <=16


# Napsiz funkcje validate_ip, która sprawdza, czy podany ciag znaków jest poprawnym adresem IPv4. Adres IPv4 powinien skłądać się z czterech sekcji  liczba od 0 do 255, oddzielonych kropkami.

#adres = ("255.255.255.255")

#def validate_ip(adres):
#    parts = adres.split('.')
#    if len(parts) != 4:
#        return False
#    for part in parts:
#        if not part.isdigit() or not 0 <= int(part) <= 255:
#            return False
#    return True

#print(validate_ip('192.167.1.1'))  #git
#print(validate_ip('192.167.1'))    # nie git



