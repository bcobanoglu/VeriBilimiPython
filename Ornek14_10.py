'''
Örnek 14.10: Girilen bir tarih istenilen formatta (‘28/12/2020’ gibi) ise ‘geçerli’
değilse ‘geçersiz’ mesajı veren bir programı kodlayınız.
'''
import re
gir = input("Doğum tarihi (gün/ay/yil): ")
#‘DD-MM-YYYY’ formatı için sorgulama yapan regex ifadesi
regex = r"^((3[01]|[12][0-9]|0[1-9])/1[0-2]|0[1-9])/[0-9]{4}$"
sonuc = re.match(regex, gir) #girilen eşleşiyor mu?
if(sonuc):
    print ("Geçerli Tarih")
else:
    print ("Geçersiz Tarih")