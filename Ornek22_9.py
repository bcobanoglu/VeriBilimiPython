'''
Örnek 22.9: Bir zaman damgasındaki (Timestamp) verileri ayrıştıran programı
kodlayalım.
'''
import pandas as pd
#Bir zaman damgası tanımlayalım
zd = pd.Timestamp('2021-07-09 2:40:24.50')
print("Zaman damgası.:", zd)
#--------------------------------------------
print("Yıl.:",zd.year)
print("Ay.:",zd.month)
print("Gün.:",zd.day)
print("Saat.:",zd.hour)
print("Dakika.:",zd.minute)
print("Saniye.:",zd.second)
#--------------------------------------------
print("Yılın günü.:",zd.dayofyear)
print("Ayın günü.:",zd.daysinmonth)
print("Haftanın günü.:",zd.dayofweek)
print("Haftanın günü adı.:",zd.day_name())
print("Saati yuvarla.:",zd.ceil("h"))