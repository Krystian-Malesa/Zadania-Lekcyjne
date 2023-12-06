# *: Dopasowuje 0 lub wiecej wystąpień poprzedzającego znaku.
# +: Dopasowuje 1 lub wiecej wystąpień poprzedzającego znaku.

# .: Dopasowuje




















# python -m ensurepip --upgrade
# pip install regex

import re

# txt = "Dopasowuje pozyję, która nie jest granicą słowa."
# x = re.search("^Dopasowuje.*słowa.$",txt)
# print(x)

# findall - Zwaraca liste zawierającą wszystkie wystąpienia
# search - Zwraca obiekt match, jeśli w dowolnym miejscu znajdzie dopasowanie
# split - zwraca listęm, w której ciągu znaków został podzielony przy każdym dopasowaniu
# sub - zastępuje jedno lub wiecej wystąpień

# [a-z] - zwraca dopasowania pasujące do wzorów od a-z, małe litery 
# [a-k] - zwraca dopasowania pasujące do wzorów od a-k, małe litery 
# [^michal] - wszystkie poza tymi 
# [0-9]
# [678] - mozliwe tylko takie cyfry  
# [0-6][0-9] -> 56/72
# [+] - zwraca dowolny znak 


txt = "dopniewuje nie poznieycję, która nie jest grannieicą nie słowa"
x=re.findall("nie",txt ,1)
print(x)

x=re.split("\s",txt)
print(x)

x=re.sub("nie", "WOW", txt)
print(x)

x = re.findall(r"\bnie\b",txt)
print(x)

x = re.findall(r"[\w\.]+",txt)
print(x)

mail = "Jakub.chmielak@pw.edu.pl"
x = re.match("^[\w\.]+@[\w\.]+",mail)
print(bool(x))


txt = "Rok 2023 bedzie lepszy."

x = re.sub("\d","X",txt)
print(x)


x = re.findall(r"^\b[n]\w+",txt)
print(x)

kot = "Nasz kot ma 6 lat i waży 4 kg"
x = re.findall(r"\d+", kot)
print(x)

x = re.search(r"^nasz", kot, re.IGNORECASE)
print(x)


numer = "Mój numer to 605-456-7890"

x = re.search(r"\d{3}-\d{3}-\d{4}",numer)
print(x)

# [4-8] dlatego jest napisane bo to bo telefony bo nie ma telefonów zaczynających się od 1,2,3 i 9
x = re.search(r"\b[4-8][0-9]{3}-\d{3}-\d{4}",numer)
print(x)


strona = "Owiedź https://www.example.com i htttp://www.anotherdomain.org."
domain_names = re.findall(r'https?://www\.(\w+)', strona)
print(domain_names)