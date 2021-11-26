    """
W sklepie ze sprzętem AGD oferowana jest sprzedaż ratalna. Napisz program
umożliwiający wyliczenie wysokości miesięcznej raty za zakupiony sprzęt. Danymi
wejściowymi dla programu są:
cena towaru (od 100 zł do 10 tyś. zł),
liczba rat (od 6 do 48).
Kredyt jest oprocentowany w zależności od liczby rat:
od 6–12 wynosi 2.5% ,
od 13–24 wynosi 5%,
od 25–48 wynosi 10%.
Obliczona miesięczna rata powinna zawierać również odsetki. Program powinien
sprawdzać, czy podane dane mieszczą się w określonych powyżej zakresach, a w
przypadku błędu pytać prosić użytkownika ponownie o podanie danych.
    """

class Raty:
    def __init__(self, kwota, ile_rat):
        self.kwota = kwota
        self.ile_rat = ile_rat
        
    def __math__(self):
        try:
            while(self.kwota < 100 or self.kwota > 10000):
                print("Podano złą kwotę - kredyt niedostępny. ")
                self.kwota = int(input("Spróbuj jeszcze raz"))
                
            while(self.ile_rat < 6 or self.ile_rat > 48):
                print("Podano ilość rat - kredyt niedostępny. ")
                self.rata = int(input("Spróbuj jeszcze raz."))    
                
            if(self.ile_rat >= 25):
                self.kwota = self.kwota + (self.kwota / 10)
                print("Rata twojego kredytu w wariancie na {} rat wyniesie {}".format(self.ile_rat,self.kwota))
            elif(self.ile_rat >= 13 and self.ile_rat < 25):
                self.kwota = self.kwota + (self.kwota / 20)
                print("Rata twojego kredytu w wariancie na {} rat wyniesie {}".format(self.ile_rat,self.kwota))
            else:
                self.kwota = self.kwota + (self.kwota / 40)
                print("Rata twojego kredytu w wariancie na {} rat wyniesie {}".format(self.ile_rat,self.kwota))
        except ValueError:
            print("Sprawdź czy wprowadziłeś liczby całkowite")
        except TypeError:
            print("Popraw typ danych")
            
        return self.kwota

kwota = int(input("Wprowadź cenę towaru: "))
ile_rat = int(input("Wprowadź ilość rat: "))

Raty(kwota,ile_rat).__math__()


## DZIAŁAJĄCA KLASA OBLCIZAJĄCA RATY KREDYTÓW PRZY KONKRETNYCH WARIANTACH CO DO ILOŚCI RAT
'''@author: Gigas'''
