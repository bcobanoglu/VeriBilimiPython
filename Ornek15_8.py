'''
Örnek 15.8: Bir programın kaç adımda bittiği (yürütme/çalışma süresini)
monotonic saat kullanarak ölçen basit bir program yazınız.
'''
import time
t0 = time.monotonic() #kronometreyi başlat
#buraya çalışma süresi hesaplanacak fonksiyon yazılır
time.sleep(0.5) #0.5 saniye bekle
t1 = time.monotonic() #kronometreyi durdur
print('Başla : {:.2f}'.format(t0))
print('Bitir : {:.2f}'.format(t1))
print('Süre : {:.2f}'.format(t1-t0))