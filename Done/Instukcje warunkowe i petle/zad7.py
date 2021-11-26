# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:47:43 2021

@author: student1
"""

import random 
x = random.randint(1,100)
y = int(x)
typ = int(input("Podaj swoja liczbe: "))
print(y)

while(typ != y):
    if(typ > y):
        print("Podałes za duza liczbe")
        typ = int(input("Podaj swoja liczbe"))
    elif(typ < y):
        print("Podałes za mala liczbe")
        typ = int(input("Podaj swoja liczbe"))
    else: 
        print("Gratulacje, wygrałes")
