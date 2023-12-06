def iksde() -> str: 

    return "XD"

kupa = ['a', 'b']
dupa = ['c', 'd']
kupa_str = "kupa"
kupa_int = 123

string = iksde()
print(string)


def dfa() -> int:

    return 2

dwa = dfa()
print(dwa)

from datetime import datetime
# from datetime import timedelta

data1 = datetime.strptime("15.11.2013","%d.%m.%Y")
data2 = datetime.strptime("12.06.2003","%d.%m.%Y")
data3 = data2 - data1
weynik = data3.days / 365
print(abs(round(weynik,2)))



