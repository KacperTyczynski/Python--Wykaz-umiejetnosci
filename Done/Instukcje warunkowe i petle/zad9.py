'''
Napisać program, dla podanej liczby całkowitej wyświetla jej dzielniki. Przykła-
dowo, dla liczby 21 dzielniki to: 1, 3, 7, 21.

'''
liczba = int(input("Wprowadź swoją cyfrę: "))

for x in range(1,liczba):
    if liczba % x == 0:
        print(x)
print(liczba)
    

'''
@Author: Gigas
'''