'''
Örnek 12.9:
Çok biçimlilik kavramını, bir grup hayvanın ses çıkarma (konuşma) yeteneği
üzerinden açıklayan bir uygulama gerçekleştiriniz.
'''
#Üst sınıf
class Hayvan:
    def __init__(self,ad):
        self.ad = ad

#Türetilmiş alt sınıflar
class Kedi(Hayvan):
    def Konus(self):
        return 'Miyav'
class Kopek(Hayvan):
    def Konus(self):
        return 'Hav Hav'

#Ana Program
a=[Kedi('Kedi'),Kopek('Köpek')]
for i in a:
    print (i.ad+': '+i.Konus())