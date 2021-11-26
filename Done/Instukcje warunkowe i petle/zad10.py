'''
Napisać program, który sprawdza, czy podana liczba całkowita n, n > 1, jest
liczbą pierwszą.

'''

liczba = int(input("Podaj swoją liczbę: "))
count = 0
for x in range(1,liczba):
    if liczba % x == 0:
        count += 1
        
if count == 1:
    print("Gratulacje, podałeś liczbę pierwszą.")
else:
    print("Przepraszam, to nie jest liczba pierwsza. Ta liczba posiada aż {} dzielników".format(count))
    
        
'''
@Author: Gigas
'''