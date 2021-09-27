'''
Örnek 17.18: Türkiye’de Twitter'da trend (gündem) olan ilk 10 konu başlığını
ekranda listeleyen (‘TT’ listesini alan) programı kodlayalım
'''
from pytwitterscraper import TwitterScraper
tw = TwitterScraper()
tt = tw.get_trends(code="TR")
#Diğer ülkelerin ISO kodları için https://countrycode.org/
print (tt.contents[0:10])