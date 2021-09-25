'''
Örnek 8.8 (Seri toplamı):
f(x) = x + x2 + x3 + x4 + ……… + xn şeklinde verilen serinin toplamını bulan
programı kodlayalım.
'''
from math import *
X = int (input ("X değeri.:"))
Fx = 0 #seri toplam değişkeni
N = int (input ("Seri terim sayısı.:"))
for us in range (1, N+1):
    Fx = Fx + pow(X, us)

print ("Toplam.:", Fx) #Seri toplamını (Fx)