'''
Örnek 20.6: Yeni evlenen 10 çiftten 4’ünün bir yıl sonunda mutlu olup
olmadıklarını inceleyelim. Yapılan ankete göre yeni evlenenlerin bir yıl sonunda
mutlu olma olasılıkları 0.3 olarak belirlenmiştir. Buna göre binom katsayısını ve
olası binom dağılımını hesaplayan programı kodlayalım
'''
from random import *
from math import *
bK = comb(10,4)
C = bK * (0.3)**4 * (0.7)**6
print ("binom katsayısı:", bK)
print ("binom dağılımı:", C)