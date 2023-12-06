# Napisz funkcje silnia, któa oblicza silnię danej liczby.


# lista1 = [4,3,1,5]
# lista2 = [2,5,3,3]

# suma = 0
# for indeks in range(len(lista1)):
#     mnozenie = lista1[indeks] * lista2[indeks]
#     suma = suma + mnozenie 


def silnia (n):
    if n == 1:
        return 1
    else:
        return n * silnia(n-1)
    
s = silnia(20)
print(s)


from datetime import datetime
# Zwrócenie bieżącej daty i godziny:

now = datetime.now()
print(now)


# Wyświetl akutalny miesiąć jako nawzwę, np. "Listopad"

data1 = now.strftime("%B")
print(data1)

# Konwertuj napis "2023-11-15" na obiekt daty

data2= datetime.strptime("2023-11-15","%Y-%m-%d")
print(data2)



# 2023-Nov-15
data3 = datetime.strptime("2023-Nov-15","%Y-%b-%d")
print(data3)

# Dodaj 5 dni do akutalnej daty
from datetime import timedelta
print(now + timedelta(days= 5))

# odejmij 2 tygodnie od aktulanej daty 
print(now - timedelta(weeks= 5))



# Wyświetl różnice w dniach między 1 stycznia 2023 a dzisiaj
roz = datetime.strptime("1 January 2023", "%d %B %Y")
data4 = now - roz
print(data4)

# Sprawdź, czy rok 2024 jest rokiem przestępnym.
import calendar

prze = calendar.isleap(2022)
print(prze)


# Wyświetl numer bieżącego tygodnia roku.
print(now.strftime("%U"))




# Zmień format daty z "2023-11-15 00:00:00" na format RFC 2822
data6 = datetime.strptime("2023-11-15 00:00:00","%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S")
print(data6)




# Znajdź dzień tygodnia dla 4 lipca bieżącego roku

data7 = datetime.strptime("2023-07-04","%Y-%m-%d").strftime("%A")
print(data7)



# Oblicz czas, który upłynął od nowego roku do teraz w sekundach
roz = datetime.strptime("1 January 2023", "%d %B %Y")
data4 = now - roz
print(data4.total_seconds())