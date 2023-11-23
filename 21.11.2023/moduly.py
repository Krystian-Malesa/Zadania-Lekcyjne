def kalulbmi(wysokosc, waga):
    return round((waga / wysokosc**2))


wys = float(input("Podaj swoją wysokosc w metrach: "))
wag = float(input("Podaj swoją wage w kg: "))

bmi = kalulbmi(wys, wag)

if bmi <= 18.5:
    print("Niedowaga")
elif 18.5 < bmi <= 24.9:
    print("Normalna waga")
elif 25 < bmi <= 29.9:
    print("Nadwaga")
else:
    print("Otylosc")