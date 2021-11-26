'''
@Author: Gigas
Napisać program, który:

utworzy listę 10 liczb całkowitych i wypełni ją wartościami losowymi z przedziału [−10, . . . , 10],

- wypisze na ekranie zawartość listy,
- wyznaczy najmniejszy oraz największy element w liście (za pomocą min /max oraz samemu),
- wyznaczy średnią arytmetyczną elementów listy,
- wyznaczy ile elementów jest mniejszych, ile większych od średniej.
- wypisze na ekranie zawartość listy w odwrotnej kolejności, tj. od ostatniego do pierwszego (wypisze, ale nie odwróci listy).

Wszystkie wyznaczone wartości powinny zostać wyświetlone na ekranie.

Przykład:

Wylosowane liczby:
-3 9 2 -10 -3 -4 -1 -5 -10 8
Min: -10, max: 9
Średnia: -1,00
Mniejszych od śr.: 6
Większych od śr.: 3
Liczby w odwrotnej kolejności:
8 -10 -5 -1 -4 -3 -10 2 9 -3

'''
###############################################################################################
import random
lista = []

for i in range(0,10):
    i = random.randint(-10,10)
    lista.append(i)
    
print(lista)

##############################################################################################
''' - wyznaczy najmniejszy oraz największy element w liście (za pomocą min /max oraz samemu),'''
max = max(lista)
min = min(lista)
print('Największy element listyt to: {}, najmniejszy to: {}'.format(max, min))


''' Metoda "samemu" 
lista.sort()
max = lista[-1]
min = lista[0]
print('Największy element listyt to: {}, najmniejszy to: {}'.format(max, min))
'''


###############################################################################################
''' - wyznaczy średnią arytmetyczną elementów listy,'''
srednia = sum(lista)/ len(lista)

'''- wyznaczy ile elementów jest mniejszych, ile większych od średniej.'''
wieksze = 0
for i in lista:
    if(i > srednia):
        wieksze +=1
mniejsze = len(lista)- wieksze

print("Elementów większych od średniej jest {}, natomiast mniejszych jest: {}".format(wieksze,mniejsze))



################################################################################################
'''- wypisze na ekranie zawartość listy w odwrotnej kolejności, tj. od ostatniego do pierwszego 
    (wypisze, ale nie odwróci listy)
'''

print("WYŚWIETL LISTĘ W ODWROTNEJ KOLEJNOŚCI: ")
print(list(reversed(lista)))

# Sprawdzenie czy kompilacja kodu nie zmieniła początkowego stanu listy

print("WYŚWIETL LISTĘ W PIERWOTNEJ KOLEJNOŚCI: ")
print(lista)