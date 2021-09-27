'''
Örnek 15.11: Bir programın kaç adımda bittiği (yürütme/çalışma süresini)
hesaplayan Örnek 15.8’deki programı timeit modülünü kullanarak ölçen
programı kodlayınız.
'''
import timeit
import time
#test fonksiyonu
def test():
    time.sleep(0.5) #0.5 sn bekle
    baslamaZamani = timeit.default_timer()
    print("Başla :", baslamaZamani)

#Ana program
test() #test fonksiyonunu çağır
print("Geçen Zaman :",
timeit.default_timer() - baslamaZamani)