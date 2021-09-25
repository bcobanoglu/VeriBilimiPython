'''
Örnek 8.7 (Pascal Üçgeni): Binom katsayılarından oluşan bir Pascal üçgenini
ekrana yazdıran programı kodlayınız.
'''
from math import *
n = 6
for k in range(0,n):
    for a in range(0,k):
        C = comb(k, a)
        print (C, end=" ")
    print("1") # yanına 1 ekle ve alt satıra geç