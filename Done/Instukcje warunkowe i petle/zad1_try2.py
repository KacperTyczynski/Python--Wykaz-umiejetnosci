'''
#$$$$$#######################  KOD FUNKCJONALNY POTRZEBNY DO WYKONANIA ZADANIA ############################################$$$$$

waga = float(input("Wprowadź swoją wagę: "))
wzrost =  float(input("Wprowadź swój wzrost: "))
wzrost = wzrost ** 2

def BMI(waga, wzrost):
    math = (waga/wzrost)*10000    
    print("Twój współczynniik BMI wynosi {:.2f}% ".format((math)))
    return math
liczenie = BMI(waga, wzrost)

if(liczenie >= 24.9):
    print("Masz nadwagę")
elif(liczenie <= 18.5):
    print("Masz niedowagę")
else:
    print("Masz właściwą wagę")
    
#$$$$$#######################  KOD FUNKCJONALNY POTRZEBNY DO WYKONANIA ZADANIA ############################################$$$$$
    
'''

class BMI:
    def __init__(self, waga, wzrost):
        self.waga = waga
        self.wzrost = wzrost
        
    def __math__(self):
        math = float((self.waga/self.wzrost**2)*10000) 
        print("Twój współczynniik BMI wynosi {:.2f}% ".format((math)))          
        
        if (math > 24.9):
            print("Masz nadwagę")
        elif(math <= 18.5):
            print("Masz niedowagę")
        else:
            print("Masz właściwą wagę")
        
    
waga = float(input("Wprowadź swoją wagę: "))
wzrost = float(input("Wprowadź swój wzrost:  "))
BMI(waga, wzrost).__math__()

# W PEŁNI DZIAŁAJĄCA KLASA SŁUŻACA DO WYLICZENIA WSPÓŁCZYNNIKA BMI
"""@author: Gigas"""