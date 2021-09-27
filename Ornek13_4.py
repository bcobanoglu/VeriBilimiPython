'''
Örnek 13.4:
Personel sınıfındaki bir çalışanın kimliğini @property dekoratörü ile bir özellik
gibi doğrudan atama yapılarak değiştiren ve silen programı kodlayalım.
'''
class Personel:
    def __init__(self, a, s):
        self.ad = a
        self.syd = s
    
    @property
    def kimlik(self):
        return f'Kimlik değişti:\n{self.ad} {self.syd}'
    @kimlik.setter
    def kimlik(self, isim):
        #kimlikten ad soyad bilgileri ayrıştırıldı
        ad, syd = isim.split(' ')
        self.ad = ad
        self.syd = syd
    @kimlik.deleter
    def kimlik(self):
        del self.syd

#Ana program
calisan = Personel('bulent','coban')
print ("Adı.:", calisan.ad)
print ("Soyadı.:", calisan.syd)
''' Başına @property dekoratörü getirilen kimlik metoduna bir özellik
(değişken) gibi doğrudan değer ataması yapıldı.'''
calisan.kimlik = 'levent can'
print ("Adı.:", calisan.ad)
print ("Soyadı.:", calisan.syd)
#şimdi syd özelliği silindi
del calisan.syd
#silinen özelliğe erişmeye çalışırken hata mesajı alınır.
print ("Soyadı.:", calisan.syd)