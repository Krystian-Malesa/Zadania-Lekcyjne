def Euklides(a,b):
    while a!= b:
        if a > b :
            a -= b
        else:
            b -= a
    return a

print(Euklides(18,12))

# inny sposob


# def Euk(a,b):
#     while b:
#         a , b = b, a % b
#     return a
# print(Euk(16,12))