'''
Örnek 12.5:
Kalıtım konusunu daha iyi anlamak için örneğimizi kodlayalım
'''
class Araba():
    #yapıcı metot ve parametreleri
    def __init__(self, hiz, renk):
        self.hiz=hiz
        self.renk=renk
    def __str__(self):
        return "Hız: {}\nRenk: {}".format(self.hiz,self.renk)
    def calis(self):
        print ("Çalışıyor...")
    def dur(self):
        print("Duruyor...")

#Araba sınıfından kalıtımla Kamyon sınıfı türetildi
class Kamyon(Araba):
    def __init__(self, hiz, renk):
        Araba.__init__(self, hiz,renk)

#Araba sınıfından kalıtımla Taksi sınıfı türetildi
class Taksi(Araba):
    def __init__(self, hiz, renk, vites):
        Araba.__init__(self, hiz,renk)
        self.vites=vites #yeni özellik eklendi
    def __str__(self):
        return Araba.__str__(self)+"\nVites.:"+str(self.vites)

#Ana program
k=Kamyon(80,"Mavi")
print ("Kamyon\n",k)
k.dur()
print("---------------------")
t=Taksi(110,"Sarı","Otomatik")
print ("Taksi\n",t)
t.calis()