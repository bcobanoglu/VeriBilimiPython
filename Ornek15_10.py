'''
Örnek 15.10: Bir önceki doğrusal arama fonksiyonunun performansını timeit
modülünü kullanarak hesaplayan programı kodlayınız.
'''
import timeit as t
import random
bulundu = False
def dogrusalArama(sayi): #doğrusal arama algoritması
    global bulundu
    #[1-10bin] arası 9999 sayıyı rastgele üret
    liste = random.sample(range(1, 10000), 9999)
    if sayi in liste:
        bulundu = True

#Ana program
sayi = 1453 #aranan sayı
print("Çalışma süresi:")
print(t.timeit(stmt="dogrusalArama(sayi)", setup="from __main__ import dogrusalArama, sayi",number=1))
print (bulundu)