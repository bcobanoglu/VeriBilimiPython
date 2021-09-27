'''
Örnek 13.7: Soyut sınıf ve metot kavramını bir önceki örnek uygulama
üzerinden açıklayalım.
'''
from abc import *
class Pizza(ABC): #üst soyut sınıf
    icerik = ['Peynir', 'Zeytin']
    
    @classmethod #sınıf metodu
    @abstractmethod #soyut metot
    def getMalzeme(cls):
        return cls.icerik

#DiyetPizza sınıfı Pizza sınıfının metotlarına sahip olmalıdır
class DiyetPizza(Pizza): #alt sınıf
    @classmethod #sınıf metodu
    def getMalzeme(cls):
        return ['Mantar'] + cls.icerik

#Ana program da
#Örnek oluşturmadan sınıf metoduna erişebiliriz
print(DiyetPizza.getMalzeme())