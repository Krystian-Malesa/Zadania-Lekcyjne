# Ćwiczenie z Pythona: Napisz pseuokod algorytmu, a następnie przekształć go w kod Pythona,
# który sortuje listę liczb metodą bąbęlkową.
# - wejscie: tablica (array)
# - wyjscie: tablica (array)

import time
import random

tablica = [2,3,1,4]
numer = len(tablica)


def sortowanie(tablica): 
    for i in range(numer-1):
        for j in range(numer-i-1):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
                print(tablica)

sortowanie(tablica)
        
ile = 1000000
arr = [random.randint(1,ile) for _ in range(ile)]
start_time = time.time()
sortowanie(arr)
end_time = time.time()
print("Czas wykonania sortowania przez wstawianie dla zbioru" , ile, "to", end_time-start_time, "sekund")
        