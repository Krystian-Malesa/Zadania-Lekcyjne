# Napisz funckję w Pythonie, która przyjmuje liczbę całkowitą jako 
# argument i zwarca listę wszystkich jej dzielników
# wejście: 1 liczbę całkowitą
# wyjscie: lista/tablica

def dzil(a):
    lista = []
    for i in range(1,a+1):
        if a % i==0:
            lista.append(i)
    print(dzil)


dzil(10)
