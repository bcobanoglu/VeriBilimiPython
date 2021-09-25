'''
Örnek 7.10.
Yukarıda kendi oluşturduğumuz ‘pyPaketim’ içerisindeki modüllerde yer alan
fonksiyonları başka bir programa import ederek (ekleyerek) çalıştıralım.
'''
from pyPaketim import *
#Kitap.py modulü içerisindeki fonk. erişelim
Yazar("Ali")
#HesapMakinesi.py içerisindeki fonksiyonlarım
print("3^2 : ", Us(3,2))
print("3/2 : ", Bol(3,2))
print("3-2 : ", Fark(3,2))
print("3+2 : ", Topla(3,2))