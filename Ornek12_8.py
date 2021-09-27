'''
Örnek 12.8:
Kapsülleme (Encapsulation) kavramını TV örneği üzerinden açıklayan bir
uygulama gerçekleştiriniz.
'''
class TV:
    def __init__(self, ses):
        self.s = ses
        self.__sesGuncelle()
    def acik(self):
        print ("TV açık")
    def __sesGuncelle(self):
        print ("Ses güncellendi.:", self.s*self.s)
#Ana Program
lg = TV(5)
lg.acik()
#lg.__sesGuncelle() erişilmez