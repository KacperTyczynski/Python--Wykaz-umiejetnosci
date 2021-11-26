'''
Napisać program, który pobiera od użytkownika ciąg liczb całkowitych. Pobieranie

danych kończone jest podaniem wartości 0 (nie wliczana do danych). W następ-
nej kolejności program powinien wyświetlić sumę największej oraz najmniejszej z

podanych liczb oraz ich średnią arytmetyczną.
Przykład:
Użytkownik podał ciąg: 1, -4, 2, 17, 0.
Wynik programu:
13 // suma min. i maks.
6.5 // średnia

'''

lista = []
cyfra = int(input("Podaj liczbę: "))
while(cyfra !=0):
    lista.append(cyfra)
    cyfra = int(input("Podaj liczbę: "))
else:
    suma = min(lista) + max(lista)
    srednia = suma / 2
    print("Suma największej i najmniejszej liczby z listy wynosi: {}, natomiast ich średnia wynosi: {}".format(suma, srednia))
    
    
'''@author: Gigas'''