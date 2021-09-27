'''
Örnek 17.14. urllib.request modülü: Metin (text) formatındaki bir web
sayfasından (sayfa.txt uzantılı olabilir) verileri çeken (ekrana yazan) programı
kodlayınız
'''
import urllib.request
#Text içerikli bir web adresi gir
adres = "http://shallowsky.com/python/lesson2.txt"
#web adresini aç
f = urllib.request.urlopen(adres)
# Okuduğunu string formatında dosya değişkeninde tut
dosya = f.read(110).decode() #ilk 110 karakteri al
print (dosya) #ekranda göster