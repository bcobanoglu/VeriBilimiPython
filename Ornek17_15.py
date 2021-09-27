'''
Örnek 17.15. BeautifulSoup modülü: Bir web sayfasından sayfa başlığı,
başka bir sayfaya bağlantı içeren linkleri ve tüm metin içeriği verilerini çeken
(ekrana yazan) programı kodlayınız.
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
adres = "http://shallowsky.com/python"
page = urlopen(adres)
dosya = page.read().decode("utf-8")
s = BeautifulSoup(dosya, "html.parser") #html sayfası parse et
# xml sayfasını parse etmek için ‘html.parser’ yerine ‘lxml’ veya ‘lxml-xml’ ifadeleri yazılabilir
#Belli bir tag <head> arasındakileri listelemek için;
print (s.find('head'))
print ("Web sitesi başlık etiketi:", s.head.contents)
print ("Site başlığı: ", s.title.string)
'''başka bir sayfaya geçiş sağlayan linkleri (<a> etiketi içeren metinleri) listelemek için;'''
print ("Başka bir web sayfasına bağlantı adresleri: ")
for link in s.find_all('a', limit=8): #ilk 8 tanesi
    print(link.get('href')) #limit belirtilmez ise tümünü listeler
'''
#bir web sitesinin kaynak kodunu almak için;
print (s.html.parent)
#Web sitesinin tüm text içeriğini çekmek için;
print(s.get_text())
'''