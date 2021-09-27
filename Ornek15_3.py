'''
Örnek 15.3: İki tarih arasındaki gün sayısını hesaplayan programı yazınız.
'''
from datetime import date
tarih1 = date.today() #bugünkü tarihi al
print ("Bugünkü Tarih:",tarih1)
yil=int(input("Yılı gir:"))
ay=int(input("Ayı gir:"))
gun=int(input("Günü gir:"))
tarih2= date(yil,ay,gun) #girilenleri tarih formatına dönüştür
fark=tarih1-tarih2
print ("İki tarih arası:", fark.days, "gündür")