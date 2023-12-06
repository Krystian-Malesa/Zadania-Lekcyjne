#!/bin/bash

# echo "Pierwszy argument: $1"

# suma=$(($1+$2))

# echo "Suma: $suma"




echo "liczba parametrów: $#"
if [ $# -ne 2 ]; then
    echo "Podaj dokladnie 2 parametry"
    exit
fi

if [ "$1" == "lista" ]; then
    ls -la
fi
