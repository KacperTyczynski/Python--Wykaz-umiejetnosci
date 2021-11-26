# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:01:44 2021

@author: student1
"""

lista= []
print("podawaj liczby. Liczba zero kończy ciąg")
liczba = int(input("Podaj pierwszą liczbe:  "))

while(liczba != 0):
    liczba = int(input())
    if(liczba != 0):
        lista.append(liczba)
        
lista.sort()
print(lista[0], lista[-1])
suma = lista[0]+lista[-1]
srednia = suma/2

print("Suma to {0}, srednia to {1}".format(suma,srednia))

