'''
Örnek 20.2:
1-10 arası rastgele sayılardan oluşan N elemanlı bir veri kümesinin aritmetik,
geometrik ve harmonik ortalamasını hesaplayan programı kodlayalım.
'''
from random import *
from math import *
from statistics import *
N = int (input("N değeri.:"))
L=[]#bos liste
for i in range(N):
    a = randint(1,10)
    L.append(a) #a'yı listeye ekle
print ("Veri grubu:", L)
print ("Aritmetik ortalama:", mean(L))
print ("Geometrik ortalama:", geometric_mean(L))
print ("Harmonik ortalama:", harmonic_mean(L))