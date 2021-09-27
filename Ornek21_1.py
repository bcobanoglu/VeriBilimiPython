'''
Örnek 21.1. (Farklı şekillerde vektör (dizi) tanımlamaları):
0-10 (dahil) arası çift sayılardan ve 0, 1 , 6 rakamlarından oluşan dizileri farklı
şekillerde oluşturup ekranda gösteren programı kodlayınız.
'''
import numpy as np
d1 = np.array([0,2,4,6,8,10])
d2 = np.arange (0, 12, 2)
d3 = np.linspace(0, 10, 6)
d4 = np.full(4,6)   #4 elemanlı 6 rakamlarından oluşan dizi
d5 = np.zeros(4)    #4 elemanlı 0 rakamlarından oluşan dizi
d6 = np.ones(4)     #4 elemanlı 1 rakamlarından oluşan dizi
print (d1, "\n", d2)
print (d3, "\n", d4)
print (d5, "\n", d6)