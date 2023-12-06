#!/bin/bash

#if [ "$1" == "plik" ]; then
#    touch = "$2"
#    echo "Utwórz plik $2"
#elif [ "$1" == "katalog" ]; then
#    mkdir "${2:-"plik.txt"}"
#    # mkdir "$2"
#    echo "Utworzono katalog $2."
#else
#    echo "Nie znana akcja."
#fi




# $1 - zmienna 1
# $# - ilosc zmiennych 
# $@ - zbiorem zmiennych

#for arg in "$@"; do
#   echo "Argument: $arg"
#done


for (( i=$#; i>0; i--)); do
    echo "Argmunet $i"
done