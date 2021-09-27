'''
Örnek 18.3:
Bir önceki örnekte oluşturduğumuz tablo üzerinde sorgular yapan (adı ‘Berat’
olanı ‘İsmail’ olarak değiştiren, adresi ‘S’ ile başlayan kayıtları listeleyen) bir
programı kodlayınız.
'''
import sqlite3
bgln = sqlite3.connect('personel.db')
vt = bgln.cursor()
#sorgu1: musteri tablosundaki tüm kayıtları listele
for kay in vt.execute('SELECT * FROM musteri'):
    print(kay)
#sorgu2:Adı 'Berat' olan kaydı 'Ismail' olarak #güncelle/değiştir
sorgu2 = vt.execute("update musteri set ad='Ismail' where ad='Berat'")
print ("------------------------")
#sorgu3:Adresi 'S' ile başlayan tüm kayıtları listele
sorgu3 = vt.execute('SELECT * FROM musteri WHERE adres LIKE "S%"')
for kayitlar in sorgu3:
    print(kayitlar)
bgln.commit()   #veritabanını kaydet
bgln.close()    #veritabanını kapat