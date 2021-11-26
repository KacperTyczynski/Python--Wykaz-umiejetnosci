'''
Napisać program, który pobiera od użytkownika liczbę całkowitą, a następnie:
oblicza sumę cyfr tej liczby,
stosunek średniej arytmetycznej cyfr parzystych do średniej arytmetycznej
cyfr nieparzystych.

'''
try:
    cyfra = int(input("Wybierz dowolną liczbę całkowitą:  "))
except ValueError:
    print("Nie podałeś liczby całkowitej")


'''##################### OBLICZANIE SUMY CYFR W LICZBIE  ################################'''

stringInt = str(cyfra)
suma = 0
parzyste = [ ]
nieparzyste = [ ]

for i in range(0,len(stringInt)):
    n = int(stringInt[i])
    if(n%2 == 0):
        parzyste.append(n)
    else:
        nieparzyste.append(n)
    suma +=n

print("Suma wszystkich cyfr w liczbie {} wynosi {}".format(cyfra,suma))

'''##################### WYLICZANIE ŚREDNIEJ NA PODSTAWIE PARZYSTOŚCI LICZBY ######################'''

sredniaP = sum(parzyste) / len(parzyste)
sredniaN = sum(nieparzyste) / len(nieparzyste)

stosunek = sredniaP/sredniaN
print("Średnia arytmetyczna liczb parzystych wynosi: {:2f}, średnia arytmetyczna liczb nieparzystych wynosi: {:2f}, stosunek tych średnich wynosi: {:2f}".format(sredniaP,sredniaN, stosunek))



'''@author: Gigas'''



