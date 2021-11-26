# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:53:09 2021

@author: student1
"""


from random import randint

lista2 = [randint(1,10) for x in range(20)]
print(lista2)
slow = {}



def licz_liczby(lista):
   licznik = {}
   for x in lista:
       if x in licznik:
           licznik[x] +=1
       else:
           licznik[x] = 1

def wyswietl_slownik(licznik):
    for klucz in licznik:
        print(klucz, ":", licznik[klucz])
           
wynik = licz_liczby(lista2)
wyswietl_slownik(wynik)  
 
           
    