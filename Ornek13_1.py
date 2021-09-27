'''
Örnek 13.1:
Sınıf içerisinde @staticmethod kullanımını Pizza örneği üzerinden açıklayan bir
programı kodlayalım.
'''
import math
#Pizza sınıfı
class Pizza:
    def __init__(self, r, icerik):
        self.r = r
        self.icerik = icerik
    
    def __repr__(self):
        return (f'{self.icerik}')
    
    def Alan(self):
        return self.Boyut(self.r)

    @staticmethod
    def Boyut(r):
        return round (r ** 2 * math.pi)

#Ana program
p = Pizza(4, ['peynir', 'domates', 'mantar'])
print ("Pizza İçindekiler: ", p)
print ("Büyüklük: ", p.Alan())