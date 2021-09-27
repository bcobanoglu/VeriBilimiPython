'''
Örnek 12.7:
Çoklu kalıtım konusunu daha iyi anlamak için örneğimizi kodlayalım.
'''
class Anne():
    #yapıcı metot ve parametreleri 
    def __init__(self, ana):
        self.ana = ana
       
    def __str__(self):
        return "Anneden:" + self.ana
class Baba():
    #yapıcı metot ve parametreleri 
    def __init__(self, aba):
        self.aba = aba
       
    def __str__(self):
        return "Babadan:" + self.aba
   
#Anne ve Baba sınıfından çoklu kalıtımla Evlat sınıfı türetildi
class Evlat(Anne, Baba):
    def __init__(self, ana, aba, alinTerim):
        #Anne ve Baba sınıfından örnekler oluşturuldu
        Anne.__init__(self, ana)
        Baba.__init__(self, aba)
        self.alinTerim = alinTerim
    def __str__(self):
       	return Anne.__str__(self)+"\n"+Baba.__str__(self)\
	           +"\nAlın terim:"+str(self.alinTerim)
             
#Ana program    
print("----Mirasım-----")
miras = Evlat("Zeytinlik","Villa","Diploma")
print (miras)
