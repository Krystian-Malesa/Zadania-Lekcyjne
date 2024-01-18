whoami # Jaki jest uzytkownik zalogowany
ls, cp, rm, chmod, chown, mv, mkdir, cd, touch, sudo, pwd, cat, adduser, newgrp, passwd

ls -la | grep nazwa_katalogu

grep 'tekst' nazwapliku.txt

grep -r 'tekst' nazwakatalogu

grep -i 'tekst' nazwapliku.txt --- 'TEkst'
-n # pokazuje numer wiersza
-l

grep -l 'text' *.txt

-v # zaprzeczenie



### find ###

find nazwa_pliku
find nazwa_katalogu -perm 644
-size +10M
# wyszukuje pliki które zostały utworzone w ostatnich 10 dniach
-mtime 10

# przekierownia

> - nadpisanie lub utworzenie
ls -la > output.txt

>> - dodanie
< - wsad do polecenia
| - pipe # taki chain który łączy jeden proces z drugim procesem


# sieciowe #
ping [ip, dns]

netstat
netstat -r 
netstat -i
netstat -tuln

ipconfig
ipconfig /all

ip addr

nmap -v -A ip_address

tcpdump -i eth0



ssh user@ip
ssh ip
ssh-keygen
shh-copy-id io


scp - Secure copy
scp plik.txt user@ip:plik_zdalny.txt
scp -r -p nazwakatalogu user@op:katalogzdalny

rsync # synchroniczne kopiowanie pliku


# procesy #

ps # wyswietla aktywne procesy
ps aux

#       #

top
htop

kill
kill PID
killall

df - disk free
du - disk useage

df -h

du -sh

free -h

curl, wget

tar # służy do tworzenie archiwum, czyli umieszczania plików w jednym pliku zbiorczym
zip unzip

# ścieżki $
echo $PATH
export $Path = "/path;$PATH"


# wyswietlanie wszystkich procesów które mamy w danej powłoce #
jobs 

bg %1


# Możliwość uruchomienia kilku terminali na raz

screen 
screen -S nazwa - tworzy screena
Ctrl-A d    # Cofnąć się wcześniejszego screena
screen -ls  # wyświetla wszystkie
screen -r nazwa # usuwa screena