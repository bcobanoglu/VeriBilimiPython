'''
Örnek 20.1: Bir öğretmen 12 kişilik sınıftaki öğrencilerine kaç kardeşleri
olduğunu sordu. Aldığı cevapları aşağıdaki gibi veri setine küçükten büyüğe
yazdı:
veri_seti = [0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 7 ]
Bu veri_seti’nin modunu, medyanını ve 1. ve 3. çeyrek değerlerini hesaplayan
programı kodlayınız.
'''
from statistics import *
veri_seti=[0,1,1,2,2,3,3,3,3,4,5,7]
print ("Veri Seti:", veri_seti)
print ("Ortalama:",mean(veri_seti))
print ("Ortanca:", median(veri_seti))
print ("Mod:", mode(veri_seti))
print ("Çeyrekler:", quantiles(veri_seti))