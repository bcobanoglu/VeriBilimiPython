'''
Örnek 12.1:
Araba sınıfından ‘Kamyon’, ‘Taksi’ gibi nesneler oluşturup bu nesnelerin farklı
özelliklerini ekrana yazdıran uygulamayı kodlayınız.
'''
class Araba():
    # Sınıf özellikleri
    model="BMC"
    renk ="Kırmızı"
    kapi = 5
    
    # Sınıf fonksiyonları
    def calis(self):
        print ("Çalışıyor…\nHız=40")
    def dur(self):
        print("Durdu…\nHız=0")

#Ana program
kamyon=Araba() #Kamyon nesnesi üretildi
taksi=Araba() #Taksi nesnesi üretildi
#Nesnelerin bazı özellikleri değiştirildi
taksi.model="Nissan Micra"
kamyon.kapi=2
print(kamyon.model, kamyon.renk)
kamyon.dur()
print("---------------------")
print(taksi.model, taksi.renk)
taksi.calis()