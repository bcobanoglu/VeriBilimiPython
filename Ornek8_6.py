'''
Örnek 8.6 (OKEK Hesabı):
Rastgele üretilen iki sayının en küçük ortak bölenlerini (OKEK) bulan programı
kodlayalım.
'''

#OKEK(a,b) = a*b / gcd(a,b) ile hesaplanabilir
from random import *
from math import *
#Ana program
a = randint(1,100)
b = randint(1,100)
obeb = gcd(a,b) #obebini al
okek =(a*b)/obeb #okekini al
print (f"a:{a} \nb:{b} \nObeb={obeb}")
print("Okek(", a, ",", b, ")=", okek )