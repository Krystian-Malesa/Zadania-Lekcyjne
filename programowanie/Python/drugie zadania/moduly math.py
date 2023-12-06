# import math
from math import sqrt

print(sqrt(10))

import random 

# Generowanie losowje liczby całkowitej z zakresu 1-100:
print(random.randint(1,100))

# Wybór losowego elementu z listy: 
fruits = ["apple", "banana", "orange"]
print(random.choice(fruits))


# Mieszane listy:
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)


# zwórcenie bieżącego czasu w sekundach:
import time 
print(time.time())

# Zwrócenie bieżącej daty i godziny:
import datetime
now = datetime.datetime.now()
print(now)


# Napisz kod, który wypisze listę wszystkich plików w bieżącym katalogu.
import os
for file in os.listdir():
    print(file)


file_path = "request.py"
if os.path.exists(file_path):
    print('file already exists')

print(os.path.isfile(file_path))

print(os.listdir('test'))

os.rename(file_path, file_path+"nowy_plik.txt")

os.mkdir("nowy_katalog")

# Usunięcie katalogu
os.rmdir("nowy_katalog")

with open("nowy_plik.txt","w") as f:
    f.write("To jest nwoy plik.")


    