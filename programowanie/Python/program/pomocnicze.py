def usun_z_listy(listunia: list, wartosc: int):
    try:
        listunia.remove(wartosc)
        print("udalo sie")
    except:
        print(f"kupka dupka")



liczbe = 10
while liczbe > 0:
    print("gowno")
    liczbe -= 1
lista_liczb = {2,6,3,4}
gowno=sum(lista_liczb)
print(gowno)

