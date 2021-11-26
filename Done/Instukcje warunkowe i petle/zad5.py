# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:57:17 2021

@author: Gigas
"""
try:
    liczba = int(input("Podaj liczbe: "))
    suma = 0
    while(liczba != 0):
        suma += liczba
        liczba = int(input("Podaj liczbe: "))
    else:
        print(suma)
except ValueError:
    print("Nie podałeś żadnej liczby- nie ma czego sumować")