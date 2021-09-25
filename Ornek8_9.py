'''
Örnek 8.9 (Sin() fonksiyonunun Maclaurin seri açılımı hesabı):
Şeklinde ifade edilen f(x) fonksiyonu sin(x) değerini hesaplayan Maclaurin seri
açılımıdır. Bu seriyi hesaplayan programı kodlayalım
'''
#Maclaurin serisi
from math import *
N = 19 # seri terim sayısı
isrt = -1
T = 0
X = int (input ("X değeri.:"))
print ("Sin(", X, ") = ", end ='')
# X değerini radyana çevirelim
X = radians(X)
for i in range (1,N,2):
    isrt = -1 * isrt
    T = T + isrt * (X**i) / factorial(i)
print (T)