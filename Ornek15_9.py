'''
Örnek 15.9:
9999 elemanlı bir listede doğrusal arama yapan bir fonksiyonun performansını
CPU çalışma süresi üzerinden hesaplayan bir programı kodlayınız.
'''
import time
import random
bulundu = False
def dogrusalArama(sayi): #doğrusal arama algoritması
    global bulundu
    #[1-10bin] arası 9999 sayıyı rastgele üret
    liste = random.sample(range(1, 10000), 9999)
    if sayi in liste:
        bulundu = True

#Ana program
t0 = time.process_time()
dogrusalArama(523) #aranan sayı
t1 = time.process_time()
print ('CPU Çalışma Süresi:', (t1-t0),'sn')
print (bulundu)