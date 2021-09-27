'''
Örnek 15.5: Doğum gününüze kaç gün kaldığını hesaplayan bir uygulama
gerçekleştiriniz.
'''
from datetime import date
bugun = date.today() #bugunku tarih
print ("Bugünkü Tarih:",bugun)
#sadece doğum tarihinin ay ve gününü gir
dogumGunu = date(bugun.year, 10, 17)
print ("Doğum günüm:",dogumGunu)
#Eğer doğum günün geçti ise
if dogumGunu < bugun:
    #bugünkü yılı 1 artır
    dogumGunu = dogumGunu.replace(year=bugun.year + 1)

#iki tarih arasındaki farkı hesapla
kalanGun = abs(dogumGunu - bugun)
print("Doğum günüme", kalanGun.days, " gün kaldı")