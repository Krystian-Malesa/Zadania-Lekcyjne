import os

def check_file_exists(file_path):
    return os.path.exists(file_path)

def read_fields():
    with open(file_path, 'r') as file:
        return file.readlines()

def display_fields():
    all_fields = read_fields()
    for linia in all_fields:
        suma_powierzchni = 0
        wymiary = linia.split(";")[1].strip()
        imie = linia.split(";")[0]
        lista_wymiarow = wymiary.split(",")
        for dzialka in lista_wymiarow:
            if dzialka:
                wymiary_dzialki = dzialka.split("X") 
                powierzchnia = calculate_field_area(float(wymiary_dzialki[0]),float(wymiary_dzialki[1]))
                suma_powierzchni += powierzchnia
        print(f"{imie}, {lista_wymiarow}, Suma powierzchni dzialek wynosi = {suma_powierzchni} ")
    

def calculate_field_area(lenght:float,width:float) -> float:
    # Oblicza powierzchnię działki
    powierzchnia = lenght * width
    return powierzchnia

def format_fields_data(fields):
    # Formatuje dane o działkach do zapisu w pliku.
    dzialki = ""
    for entry in fields:
        dzialki += f"{entry[0]}X{entry[1]}, "
    return dzialki



def add_entry(nazwa_rolnika,fields):
    all_fields = read_fields()
    for linia in all_fields:
        if nazwa_rolnika in linia:
            print("Juz jest")
            return False
        
    zformatowane_fields = format_fields_data(fields) 
    entry = f"{nazwa_rolnika}; {zformatowane_fields}\n"
    all_fields.append(entry)
    print("Rolnik został dodany")
    save_fields(all_fields)


def save_fields(fields) -> list:
    with open(file_path,'w') as file:
        for linia in fields:
            file.write(linia)


file_path = "dzialki.txt"
fields = [
    (1.0 , 4.0),
    (53.3 , 12.2)
]
# add_entry("Zygmunt1",fields)
# print(format_fields_data(fields))
display_fields()

