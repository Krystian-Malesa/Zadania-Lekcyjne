from datetime import datetime
import os

def validate_phone_number(phone_number):
    # Sprawdza, czy podany numer telefonu jest prawidłowy, tj. czy składa się z dokładnie 9 cyfr
    return len(phone_number) == 9 and phone_number.isdigit()


def check_file_exists(file_path):
    # Sprawdza, czy podany plik istnieje.
    return os.path.exists(file_path)


def get_appointments_from_file(file_path) -> list:
    # Wczytuje i zwraca listę zapisanych wizyt z pliku.
    with open(file_path,'r') as file:
        return file.readlines()


def check_availability(appointments, date):
    # Sprawdza, czy jest dostępny termin na podaną datę (maksymalnie 8 wizyt na dzień).
    try:
        datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        print("zła data")
        return False
    
    appointments = get_appointments_from_date(appointments, date)
    if len(appointments) < 8:
        return True
    else:
        return False




def save_appointment(file_path, phone_number, date, time):
    # Zapisuje dane wizyty w pliku, jeśli numer telefonu jest prawidłowy i istnieje dostępny termin.
    if not validate_phone_number(phone_number):
        print("Zły numer")
        return False
    
    appointments = get_appointments_from_file(file_path)
    if not check_availability(appointments, date):
        print("wizyta juz istnieje")
        return False
    
    with open(file_path, 'a') as file: 
        file.write(f"{phone_number};{date}:{time}\n")
        print("wizyta zapisana")
        return True

def get_appointments_from_date(appointments, date):
    day_appointments = []
    for linia in appointments:
        if linia.strip(";")[1] == date:
            day_appointments.append(linia)
    return day_appointments






def show_available_hours(appointments, date):
    # Wyświetla listę dostępnych godzin wizyt na podaną datę.
    working_hours = ["8:00", "9:00","10:00", "11:00","12:00", "13:00","14:00", "15:00",]
    wybrane_godziny = get_appointments_from_date(appointments, date)
    for godzina in wybrane_godziny:
        godzina.split(";")[2].strip()
        working_hours.remove(godzina)
    print(working_hours)