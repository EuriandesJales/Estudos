#!/bin/bash
#muda o gama da tela (Caso o seu so nao consiga fazer isso automaticamente)
#randr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1
#versao 1.0

echo digite um valor para o brilho
read=$brilho
brightctl set %$brilho
#xrandr --output eDp-1 --brightness 0.$brilho
