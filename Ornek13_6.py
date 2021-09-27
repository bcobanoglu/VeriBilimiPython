'''
Örnek 13.6: Soyut sınıf ve @abstractmethod kullanımını Pizza örneği üzerinden
açıklayan programı kodlayalım.
'''
from abc import *
class Pizza(ABC): #üst soyut sınıf
    icerik = ['Peynir', 'Zeytin']
    
    @abstractmethod
    def getMalzeme(self): #soyut metot
        pass #Eşdeğeri: return

#DiyetPizza sınıfı Pizza sınıfının metotlarına sahip olmalıdır
class DiyetPizza(Pizza): #alt sınıf
    def getMalzeme(self):
        return ['Mantar'] + self.icerik

#Ana program
p = DiyetPizza()
print(p.getMalzeme())
