'''
Örnek 13.5:
Bir önceki bölümde çok biçimlilik kavramını açıklarken verdiğimiz 'Hayvan' üst
sınıfından, ‘Köpek’ ve ‘Kedi’ alt sınıflarını soyut sınıf ve metotlarla oluşturan
programı kodlayalım.
'''
from abc import ABC, abstractmethod
class Hayvan (ABC): #soyut sınıf tanımlaması
    @abstractmethod #soyut metot tanımlaması
    def Konus(self):
        pass

#Soyut üst sınıftan türetilmiş alt sınıflar
class Kedi(Hayvan):
    def Konus(self):
        return 'Miyav'
class Kopek(Hayvan):
    def Konus(self):
        return 'Hav Hav'

# Ana program
Ke = Kedi()     #Kedi sınıfından Ke nesnesi türetildi ve konuşturuldu
print ("Kedi.:", Ke.Konus() )
Ko = Kopek()    #Kopek sınıfından Ko nesnesi türetildi ve konuşturuldu
print ("Köpek.:", Ko.Konus() )