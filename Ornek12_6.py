'''
Örnek 12.6:
Sınıf metodunu geçersiz kılma (overriding) işlemini basit bir alan hesaplama
örneği üzerinden açıklayalım.
'''
class Dikdortgen():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Alan(self):
        print ("Alan.: ", self.a*self.b)

class Kare(Dikdortgen):
    def __init__(self, knr):
        self.knr = knr
        super().__init__(knr, knr)

    #Dikdortgen sınıfındaki Alan() metodu geçersiz kılınıyor
    def Alan(self):
        print ("Alan.: ", self.a*self.a)

#Ana program
k = Kare(4)
d = Dikdortgen(2, 4)
d.Alan() # Dikdörtgen Alanı
k.Alan() # Kare Alanı