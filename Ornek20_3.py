'''
Örnek 20.3. İlk örnekte verilen 12 kişilik sınıftaki öğrencilerin kaç kardeşlerinin olduğunu
gösteren;
veri_seti = [0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 7 ]
veri setinin aritmetik ortalamasını, örneklem varyansını ve standart sapmasını
hesaplayan programı kodlayınız.
'''
from statistics import *
from math import *
liste = [0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 7 ]
print("Veri Seti:", liste)
print("Aritmetik Ortalama:", mean(liste))
print("Varyans:", variance(liste))
print("Standart Sapma:", stdev(liste))
print("Eşdeğer Standart Sapma:", sqrt(variance(liste)))