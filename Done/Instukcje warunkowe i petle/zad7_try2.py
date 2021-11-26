''' 
Gra w ”Za dużo, za mało”. Komputer losuje liczbę z zakresu 1 . . . 100, a gracz

(użytkownik) ma za zadanie odgadnąć, co to za liczba poprzez podawanie kolej-
nych wartości. Jeżeli podana wartość jest:

większa – wyświetlany jest komunikat „Podałeś za dużą wartość”,
mniejsza – wyświetlany jest komunikat „Podałeś za małą wartość”,
identyczna z wylosowaną – wyświetlany jest komunikat „Gratulacje” i gra
się kończy.

'''

import random

pcChoice = random.randint(1,100)
userChoice = int(input("Zgadnij jaką liczbę wylosował PC: "))

while ( userChoice != pcChoice):
    if(userChoice > pcChoice):
        print("Podałeś zbyt dużą liczbę")
        userChoice = int(input("Zgadnij ponownie: "))
    elif(userChoice < pcChoice):
        print("Podałeś zbyt małą liczbę")
        userChoice = int(input("Zgadnij ponownie: "))
else:
    print("Gratulacje, odgadłeś prawidłową liczbę!")
    
'''@author: Gigas'''