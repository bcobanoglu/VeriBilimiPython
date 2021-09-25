'''
Örnek 8.1:
0 ile 100 (100 dahil) arasında 10 adet rastgele tamsayı üreten programı
kodlayalım
'''
from random import *
for _ in range (10): #10 adet
    #0-100 arasında sayı üretir
    print (randint(0,100), end=' ')