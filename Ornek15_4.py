'''
Örnek 15.4: Geçmiş tarihi bulan/hesaplayan bir program yazınız.
'''
from datetime import date, timedelta
tarih1 = date.today()
print ("Bugünkü Tarih:",tarih1)
gun= int(input("Geçmiş günü gir:"))
gecmis = timedelta(days=gun)
tarih2 = tarih1 - gecmis
print (f"{gun} gün önceki tarih.: {tarih2}")