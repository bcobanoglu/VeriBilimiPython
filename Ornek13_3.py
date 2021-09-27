'''
Örnek 13.3: Önceki bölümde Sarmalama (Encapsulation) kavramını
anlattığımız TV örneğini @property dekoratörü ile yeniden kodlayalım.
'''
class TV:
    #TV sınıfı üyeleri (özellik ve metotlar) tanımlanıyor.
    def __init__(self, s):
        self.ses = s
    
    @property
    def sesAcik(self): #getter işlemi
        return self.ses
    
    @sesAcik.setter
    def sesAcik(self, volum): #setter işlemi
        if volum > 10 and volum < 100:
            self.ses = volum
        else:
            raise ValueError ('Ses çok az ya da yüksek')

#Ana Program
lg = TV(50)
#sesAcik() metotu @property ile özelliğe dönüştü
print (lg.sesAcik)
lg.sesAcik = 110 #hata üretir