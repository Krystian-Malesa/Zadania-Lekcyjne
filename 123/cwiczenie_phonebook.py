def read_phonebook():
    # Czyta dane z pliku i zwraca je w postaci listy.
    with open(file_path,'r') as file:
        return file.readlines() 

def save_phonebook(phonebook):
    # Zapisuje dane książki telefonicznej do pliku.
    with open(file_path,'w') as file:
        for linia in phonebook:
            file.write(linia)



def display_phonebook():
    # Wyświetla aktualną zawartość książki telefonicznej.
    print(read_phonebook())

def validate_phone_number(phone_number):
    return len(phone_number) == 9 and phone_number.isdigit()

def add_entry(name, phone_number):
    # Dodaje nowy wpis do książki telefonicznej z podaną nazwą i numerem telefonu.
    # Sprawdza format numeru oraz czy numer już istnieje.
    if not validate_phone_number(phone_number):
        print("ZŁY NUMER")
        return False
    
    phonebook = read_phonebook()
    for linia in phonebook:
        if phone_number in linia:
            print("TEN NUMER JUZ ISTNEIJE")
            return False
    
    with open("book1.txt",'a') as file:
        file.write(f"{name};{phone_number}\n")
        save_phonebook(phonebook)

        

def remove_entry(phone_number):
    # Usuwa wpis na podstawie numeru telefonu.
    phonebook = read_phonebook()
    for linia in phonebook:
        if phone_number in linia:
            phonebook.remove(linia)
    save_phonebook(phonebook)


def modify_entry(old_phone_number, new_name, new_phone_number):
    # Modyfikuje istniejący wpis, pozwalając na zmianę nazwy i numeru telefonu.
    if not validate_phone_number(new_phone_number):
        print("ZŁY NUMER")
        return False
    phonebook = read_phonebook()
    for linia in phonebook:
        if old_phone_number in linia:
            phonebook.remove(linia)
            phonebook.append(f"{new_name};{new_phone_number}\n")
    save_phonebook(phonebook)




file_path = "book1.txt"
read_phonebook()
# add_entry("lol","888444553")
# add_entry("lol","888444551")
modify_entry("888444555","lol2","111111111")
display_phonebook()