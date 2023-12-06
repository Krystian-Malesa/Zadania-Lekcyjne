# Inicjalizuje nowe reporytorim Git
git init 


git clone [url] [katalog]

git clone --branch [branch-name] [url]

git clone --depth 1 [url]
1 -> ostatni commit (historia tylko jednego commitu)

git clone --mirror [url]

# Opis: Klonuje istniejące repozytorium z podanego URL.
Przykład: git clone https://github.com/przyklad/repo.git


# jezeli mamy jakas zmiane w projekcie i chcemy dodac do obszaru comitowalnego
git add [file]
git add [directory]
git add [file1] [file2]

# wstazac tylko pliki ktore maja odpowiednia koncowke:
git add ["*.py"]

# jesli chcemy dodac wszystko to:
git add .    lub   git add -A


git .ignore wrzucanie plików tymczasowych 


git commit -m ["commit message"]

# jesli chcesz zeby pulował i commitował od razu:
git commit -m -a ["commit message"]

# Korekta ostatniego commitu 
git commit --amend -m ["change last commit message"]

# Commituje z steczingu kolejny plik zeby jeszcze raz commit nie robić
git commit --amend --no-edit 

# Dodaje pusty commit 
git commit --allow-empty -m "Pusty commit"

# Dodawanie wiecej niz jednego komentarza:
git commit -m "Tytuł commita" -m "Dalszy opis zmian"

# Wyswietlenie statusu repozytorium
git status

# Wyswietla w zwarty sposob jakie pliki zostały zmienione 
git status -s

# Wyświetla wszystkie niesiedzialne "untracked" pliki
git status -u

# pokazuje informacje o bierzacej galeri 
git status -b

# Wyswietla pliki ktore sa w stashu 
git status --show-stash


# Pobiera zmiany 
git pull = git pull origin


# Na przykład konkretny branch
git pull oring dev

# Pobiera nam szczegolne informacje o procesie zmian
git pul --verbose

# symuluje proces pobierania 
git pull --dry-run

# pobierz zmiany nie w formie commitu 
git pull --no-commit ["nazwa brancha"]


# Zarządzanie zestawem śledzonych repozytoriów
git remote 
# wyswietalnie listy 
git remote -v 
# dodanie nowego repo
git remote add [nazwa] [url]
# usuwanie remota
git remote rm [nazwa]
# Zmiana nazwy
git remote rename [old-name] [new-name]
# pokazuje informacje o danym repozytorium
git remote show [shortname]
# Aktualizuje wszystkie zdane repozytoria 
git remote update
# Zmiana repozytorium
git remote set-url [shortname] [new-url]
#
git remote set-head [shortname] -a
git pull. git push


# 
git push

~ -> home
/ -> katalog główny root

                                                           # konfiguracja gita
# Najczęściej sie to robi po zainstalowaniu gita
git config --global user.name "[name]"
git conifg --global user.email "[email address]"
git config --global core.editor "[editor]"

git config --list

# Wyswietlic konkretny atrybut 
git config user.email

gig config --global alias.[alias-name] '[command]'
git config --global alias.st 'status'

# Znaki końcowe w systemach Windows i Linux
git config --global core.autocrlf [true|false|input]

# Ignoruje wielkość liter
git config --global core.ignorecase [ture|false|]

#
git config --global merge.tool [tool]

# Do porównywania zmian
git config --global diff.tool [tool]

# Zmiany uprawnień na plikach zeby byly commitowalne
git config --global core.filemode [true|false]





                                                    rebase vs merge
# MERGE Przy mergu jest commitowany ostatni branch i jest nadpisywany wlasnym commitem do MAIN

# REBASE sa przenoszone wszystkie brakujce commity do brancha głownego MAIN




                                                         BRANCHE
# wyświetlenie wszystkich branchy
Git branch

# Stworzenie brancha
git branch [branch-name]

# Usuwanie brancha lokalnie!
git branch -d [branch-name]

# Wymusza usunięcie gałęzi
git branch -D [branch-name]

# Zmienia nazwe -rename
git branch -m [old-name] [new-name]

# Wyświetlenie wszyskich zdalnych branchy
git branch -r

# Jak sprawdzic na którym branchu jesteśmy
git branch --show-current

# Branche które zostały zmerdżowane ze sobą
git branch --merged

# Lista branchy które nie zostały zmerdżowane ze sobą
git branch --no-merged [branch]

# Pokazuje tylko gałęzie, które zawierają nazwane zatwierdzenie
git branch --contains [commit]

# Jak utworzyć nowy branch z danego brancha
git branch [branch-name] [start-point]

# Skopiowanie brancha
git branch --copy feature-old feature-new

# Przenoszenie i zmiana brancha
git branch --move [old-branch][new-branch]

# Edycja opisu brancha
git branch --edit-description [branch-name]

# Wylistować branche ale z paternem
git branch --list [pattern]
git branch --list 'feature*' -> najcześniej są to regexy

# Usuwanie brancha zdalnie!
git branch --delete --remote [remote/branch]

# Wymuszenie polecenia
git branch --forece [jakies_polecenie]





                                                            Checkout
# Służa do przełączania pomiedzy branchami, zmian na branchu

git checkout [branch-name]

# Tworzenie brancha
git checkout -b [branch-name]


# Nazwa commita do którego chcemy wrocic
git checkout [commit-hash]

# Przywracanie konkretnego pliku/ wycofuje wszystkie zmiany / przywraca stan z poprzedniego commita
git checkout -- [file-name]

# Te zmiany zostaną wrzucone do nastepnego brancha
git checkout -- [branch-name] [file-name]

# Wracamy do ostatniej gałęzi
get checkout -

# Checkoutować po tagach
git checkout [tag-name]





                                                            Tagi
# To jest jakby commit na danym miejscu taki checkpoint 


git tag 

git tag [tag-name]

git tag -a [tag-name] -m '[message]'

git tag -d [tag-name]

git show [tag-name]

git push [remote] [tag-name]

git push [remote] --tags

git checkout [tag-name]

git tag -a [tag-name] [commit-hash] -m '[message]'

# Wycofywanie zmian w repozytorium
git restet [file]

# Wycofanie sie do konkretego commita
git reset --soft [commit]

# Ilosc wycofania commitów do gałęzi głównej
git reset --soft HEAD~1

# Usuwa zmiany z commita
git reset --hard [commit]

git reset --keep [commit]

