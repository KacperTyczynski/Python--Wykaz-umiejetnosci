# -*- coding: utf-8 -*-
"""
Napisać program, który wczytuje od użytkownika liczbę całkowitą dodatnią n, a
następnie wyświetla na ekranie wszystkie potęgi liczby 2 nie większe, niż podana
liczba. Przykładowo, dla liczby 71 program powinien wyświetlić:
1
2
4
8
16
32
64
@author: Gigas
"""

liczba = int(input("wprowadź swoją liczbę -- Dodatnią!   :"))

for number in range(liczba):
    potega = 2 **number
    if(potega < liczba):
        print(potega)
    