# # x =int(input("Wpisz liczba: "))
# # y =int(input("Wpisz liczba: "))

# # def kwadrat(x):
# #     return x * x
# # def kwadrat(y):
# #     return y * y


# # def bigger(x,y):
# #     if x > y:
# #         return x
# #     else:
# #         return y



# # xkw = kwadrat(x)
# # xky = kwadrat(y)
# # big = bigger(xkw,xky)

# # print(f"Z kwadratu liczb {x} i {y} wiekszą jest {big}")


# # f = "plik.txt"
# # sum = 0
# # with open(f) as fs:
# #     for n in fs:
# #         sum = sum + int(n)
# # print(sum)

# # f = "plik.txt"
# # najwieksza = 0
# # with open(f) as fs:
# #     for linia in fs:
# #         liczba=int(linia)
# #         if liczba > najwieksza:
# #             najwieksza = liczba
            
# # print(najwieksza)


# f = "plik.txt"
# najmniejsza = None
# najwieksza = None
# sum = 0
# ilosc = 0
# lista = []
# with open(f) as fs:
#     for linia in fs:
#         liczba=int(linia)
#         if najmniejsza == None or liczba < najmniejsza:
#             najmniejsza = liczba 
#         if najwieksza == None or liczba > najwieksza:
#             najwieksza = liczba
#         sum += liczba
#         ilosc += 1
#         lista.append(liczba)

# srednia = round(sum/ilosc,2)
# wynik1 = f"Najwieksza liczba to: {najwieksza}, a najmiejsza liczba to: {najmniejsza}, suma to = {sum}, srednia to = {srednia}"

# # lista = [7,5,9,54,1,21]
        
# def policz_mediane(gowno: list) -> int:
#     srodek_listy = 0
#     gowno.sort()
#     dlugosc_listy = len(gowno)
#     srodek_listy = dlugosc_listy // 2
#     return gowno[srodek_listy]

# mediana = policz_mediane(lista)

# wynik2 = f"mediana z liczb to {mediana}"


# plik = open("wynik.txt", "w")
# plik.write(wynik1+"\n") 
# plik.write(wynik2)


slownik = {
    "imie": "Krystiuan",
    "nazwisko": "Ronaldo"
}

slownik["kupa"] = "dupa"
slownik.update({"age": 199})
slownik.update({"age": 99})
slownik["age"]=1

slownik.pop("kupa")

for klucz, wartosc in slownik.items():
    print(f"klucz: {klucz} wartosc: {wartosc}")

    
for keu in slownik.keys():
    print(f"klucz: {keu}")
    
for wartosc in slownik.values():
    print(f"wartosc: {wartosc}")


car =	{
  True: "Ford",
  "model": "Mustang",
  "year": 1964
}
rok = car["year"]
print(rok)

from pomocnicze import usun_z_listy

lista = [432,532,531,123,122]
trzeci = "lista"[3]
print(trzeci)