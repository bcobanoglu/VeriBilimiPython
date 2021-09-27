'''
Örnek 16.7 (Kullanıcı tanımlı istisna örneği: benimHatam):
'''
class benimHatam(Exception):
    #Bu modüldeki tüm hataların ana sınıfı
    ad = "benimHatam.py"

class ilkHatam(benimHatam):
    #benimHatam sınıfından türetilen alt sınıf
    def __init__(self, mesaj):
        self.mesaj = mesaj
try:
    raise ilkHatam("Bu benim ilk hatam")
except ilkHatam as hata:
    print ("Affedersiniz: ",hata.mesaj)
    print ("Modul adı: ", hata.ad)