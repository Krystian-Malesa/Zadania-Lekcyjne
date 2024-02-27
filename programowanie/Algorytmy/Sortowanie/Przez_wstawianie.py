# Sortowanie przez wstawianie
import time
import random

def Sortowanie_przez_wstawianie(lista):  
    for i in range(1,len(lista)):
        zmienna = lista[i]
        j=i-1
        while j >= 0 and zmienna < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = zmienna


lista = [4,5,2,3,1]

Sortowanie_przez_wstawianie(lista)
print("posortowana lista:", lista)


ile = 1000000
arr = [random.randint(1,ile) for _ in range(ile)]
start_time = time.time()
Sortowanie_przez_wstawianie(arr)
end_time = time.time()
print("Czas wykonania sortowania przez wstawianie dla zbioru" , ile, "to", end_time-start_time, "sekund")
