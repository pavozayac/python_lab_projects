#!/bin/bash
perl -p -e "s/# Wersja2 //" ulamek.py > ulamek2.py

/usr/bin/time -v python3 ulamek.py 2000000 1000000 2>&1 1>/dev/null | grep  -E "wall|Max"
/usr/bin/time -v python3 ulamek2.py 2000000 1000000 2>&1 1>/dev/null | grep  -E "wall|Max"