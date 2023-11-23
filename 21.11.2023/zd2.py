# Napisz program obliczający wskaźnik masy ciała (BMI) na podstawie wzrostu i wagi użytkownika.

# bmi = waga / (wzrost ** 2)
import re

waga=float(input(85))
wysokosc=float(input(1.9))

bmi = waga/(wysokosc ** 2)

if bmi<18.5:
    print("Niedowaga")
elif bmi>=18.5 and bmi<24.9:
    print("Prawidłowa waga")
elif bmi>=25 and bmi<29.9:
    print("Niedowaga")
else:
    print("Otyłość")