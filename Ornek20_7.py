'''
Örnek 20.7: Hilesiz bir madeni para N=10 defa atıldığında 7 kere ‘tura’
gelmesinin olasılığı nedir? Programda ‘tura’ durumunu ‘1’, ‘yazı’ durumunu
‘0’ ile ifade edersek, toplam N atışta bu değerlerin gelme olasılığını inceleyen
programı kodlayalım.
'''
from random import *
from math import *
from statistics import *
import numpy as np
print("Yazı / Tura dağılımı")
#random 0-1 arasında kesirli sayı üretir ve
#round ile de bu sayı yuvarlatılır.
N = 7 #atış sayısı
L = [] #liste
p = 1 #tura durumu
for i in range (N):
    para = random()
    L.append(round(para))
    if para < 0.5:
        p = p + 1 #tura gelme sayısı

print (L)
#Histogram şeklinde gösterimi
print ("Tura dağılımı.:" ,"*" * p)
print ("Yazı dağılımı.:" ,"*" *(N-p))
#Varyansı
print ("Varyansı.:" , variance(L))
bK = comb(10,7) #Binom katsayısı: bK
print ("Binom katsayısı", bK)
C = bK * (0.5)**7 * (0.5)**3
print("Binom dağılımı.:", C)
print("Numpy Binom dağılımı.:",
       sum(np.random.binomial(10, 0.5, 10000) == 7)/10000)
       