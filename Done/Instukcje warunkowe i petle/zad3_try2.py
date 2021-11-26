# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26.11 10:49:20 2021

Napisać program, który pobiera od użytkownika liczbę całkowitą dodatnią, a na-
stępnie wyświetla na ekranie kolejno wszystkie liczby nieparzyste nie większe od

podanej liczby. Przykład, dla 15 program powinien wyświetlić 1, 3, 5, 7, 9, 11, 13,
15.

@author: Gigas
"""


liczba = int(input("Podaj swoją liczbę: ")) 

if (liczba <= 0):
    while(liczba < 0):
        print("Liczba ujemna, proszę wprowadzić liczbę dodatnią")
        liczba = int(input("Podaj swoją liczbę: ")) 
elif (liczba == 0):
    print("Wprowadź liczbę dodatnia - 0 nie należy do liczb dodatnik")
else:
    for i in range(0,liczba):
        if(i % 2 != 0):
            print(i)

