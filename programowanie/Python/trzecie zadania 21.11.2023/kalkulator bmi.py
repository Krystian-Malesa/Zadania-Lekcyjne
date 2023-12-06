def KalkuBmi(wysokosc:float, waga:float):
    try:
        bmi = round((waga / wysokosc**2))
        return bmi
    except ZeroDivisionError:
        return "Wzrost musi być większy od zera."
    except ValueError:
        return "Waga i wzrost muszą być liczbami"


wys = float(input("Podaj swoją wysokosc w metrach: "))
wag = float(input("Podaj swoją wage w kg: "))

bmi = KalkuBmi(wys, wag)
if bmi <= 18.5:
    print("Niedowaga")
elif 18.5 < bmi <= 24.9:
    print("Normalna waga")
elif 25 < bmi <= 29.9:
    print("Nadwaga")
else:
    print("Otylosc")
