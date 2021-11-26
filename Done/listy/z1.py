# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:56:09 2021

@author: student1
"""

import random
listaX = []
listaY = []

for xs in range(10):
    x = random.randint(-10,10)
    listaX.append(x)
    
print("Wylosowano liczby: ")
print(listaX)
   
print("Max " + str(max(listaX)) + " min " +str(min(listaX)))

dlugosc = len(listaX)
suma = sum(listaX)
    
print("Suma wszystkich cyfr z listy to:  " + str(suma))   

def srednia(lista):
    return sum(lista)/len(lista)

srednia = srednia(listaX)

print("Srednia arytmetyczna cyfr z listy to:  " + str(srednia))

wieksze = 0
mniejsze = 0

for x in listaX:
    if(x > srednia):
        wieksze +=1
    elif(x < srednia):
        mniejsze +=1
        
print("W liscie znajduje sie {0} elemntów większych niz srednia oraz {1} mniejszych od sredniej".format(wieksze,mniejsze))

for i in reversed(listaX):
    listaY.append(i)
    
print(listaY)