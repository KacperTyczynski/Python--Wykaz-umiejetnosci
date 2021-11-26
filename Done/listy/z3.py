# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:55:35 2021

@author: student1
"""

# as los --->> od teraz nazywam randint jako los
from random import randint as los
 
def wyswietl(lista):
    for wiersz in lista:
        for komorka in wiersz:
            print("%5.0f" %komorka, end= " ")
        print()

lista1 = [[los(-5,5) for x in range(5)] for x in range(5)]

wyswietl(lista1)
