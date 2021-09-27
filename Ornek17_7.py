'''
Örnek 17.7:
Bir önceki örnekteki ‘rehber.csv’ ismindeki dosyamıza yeni kayıtlar ekleyen
programı yazınız
'''
#csv modülünü import et
import csv
#yeni kayıtlar dizisi
yeniKayit=[["291;AMP9ABİ;ALİ AKSU ;ARDA AKSU;(545) 229-4921"],
            ["303;AMP9ABİ;CAN OK ;BAYRAM OK;(542) 222-4424"] ]
#'rehber.csv' dosyasını ekleme amaçlı aç
with open('rehber.csv', 'a', newline='') as f:
    ekleDosya = csv.writer(f)           #ekleDosya isimli writer nesnesi tanımlandı
    ekleDosya.writerows( yeniKayit )    #ekleDosya'ya yeni kayıtlar yazıldı