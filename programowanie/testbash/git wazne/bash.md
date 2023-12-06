# Tworzenie pliku
touch nazwa.sh

# nadawanie uprawnien
chmod +x nazwa.sh
# dodawanie uprawnien wszystko -> (a)
chmod a+x nazwa.sh

 user  grupa   owner
 drwx   rwx     rwx

# u = rwx , g=r-x , o=r--
chmod 754 nazwa.sh

chmod u=rwx, g=rx, o=r nazwa.

# Łączenie grup (dla grupy i pozostałych)
chmod go- nazwa.sh

# wszystkie pliki w katalogu z tymi uprawnieniami 
chmod -R 644 katalog/

# Odpalanie pliku
./nazwa.sh

# nadaje wszystkie uprawnienia
chmod 777

# pomoc 
chmod --help

# Wrzuc do pliku
./witaj.sh Jan > Jan.txx


# >> dopisz do pliku
np ./witaj.sh Jan >> Jan.txt


# Wszystkie kombinacje praw dostępu: 
0 - brak
1 - --x - Wykonywanie
2 - -w- - Pisanie
3 - -wx - Pisanie, wykonywanie
4 - r-- - Czytanie
5 - r-x - Czytanie, wykonanie
6 - rw- - Czytanie, pisanie 
7 - rwx - Czytanie, pisanie, wykonywanie 