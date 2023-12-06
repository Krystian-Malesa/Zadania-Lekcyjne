# Zwrócenie bieżącej daty i godziny:

from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.strftime("%Y"))

# Wyświetl akutalny miesiąć jako nawzwę, np. "Listopad"

# print(now.strftime("%A"))


# Konwertuj napis "2023-11-15" na obiekt daty

# date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
# print(date_object)

# past_date = datetime(2023, 11, 15)

# 2023-Nov-15

# date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
# print(date_object)

from datetime import timedelta
# Dodaj 5 dni do akutalnej daty
# print(now.timestamp + timedelta(days = 5))


# odejmij 2 tygodnie od aktulanej daty 
print(now + timedelta(weeks = -2))
 

# Wyświetl różnice w dniach między 1 stycznia 2023 a dzisiaj
roz_roku = datetime(2023, 1, 1)
day = now - roz_roku
print(day.days)


import calendar
# Sprawdź, czy rok 2024 jest rokiem przestępnym.
new_year = calendar.isleap(2024)
print(new_year)

# Wyświetl numer bieżącego tygodnia roku.
# print(now.strftime("%U"))


# Zmień format daty z "2023-11-15 00:00:00" na format RFC 2822
# rfc_date = datetime.strptime("2023-11-15 00:00:00 +04:00","%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S %z")
# print(rfc_date)


# Znajdź dzień tygodnia dla 4 lipca bieżącego roku
# date_object = datetime(now.year,7,4)
# print(date_object.strftime("%A"))


# Oblicz czas, który upłynął od nowego roku do teraz w sekundach

roz_roku = datetime(now.year, 1, 1)
czas_uplyniety = (now - roz_roku).total_seconds()
print(czas_uplyniety)


# Porównaj, czy data "2023-11-15" jest wczeniejsza niż dzisiaj

date1 = datetime(2023, 11, 15)

now = datetime.now()

if date1 < now:
    print("data1 jest wczesniejsza niz dzisiaj")
elif date1 > now:
    print("data1 jest pozniejsza niz data teraz")
else:
    print("data1 i data2 sa takie same")


# Formatuj datę "15/11/2023 14:30" do formatu "15 listopada 2023, godzina 14:30"


d1 = datetime.strptime("Sat 02 May 2015 19:54:36 +0530", "%a %d %b %Y %H:%M:%S %z").timestamp()
d2 = datetime.strptime("Fri 01 May 2015 13:54:36 -0000", "%a %d %b %Y %H:%M:%S %z").timestamp()
print(d1)
print(d2)
diff = d1 - d2
print(diff)