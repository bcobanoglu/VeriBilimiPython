'''
Örnek 18.2:
Öncelikle ‘personel.db’ isminde bir veri tabanı oluşturunuz. Sonrasında ise bu
veritabanı içerisinde ‘no, ad, adres’ alanlarından oluşan bir ‘musteri’ isimli tablo
oluşturup, bu tablo üzerinde sorgulamalar gerçekleştiriniz
'''
import sqlite3 #sqlite modülü çağrıldı
bgln = sqlite3.connect("personel.db")
#personel.db isimli veri tabanı tanımlandı
imlec = bgln.cursor() #imlec (kürsor) nesnesi oluşturuldu
#Eğer musteri tablosu önceden oluşturuldu ise silinsin
imlec.execute('drop table if exists musteri;')
#musteri isimli tablo oluşturuldu
imlec.execute("""CREATE TABLE musteri
(no INTEGER PRIMARY KEY, ad TEXT, adres TEXT)""")
#kayıtlar listesi
kayitlar=[  (1, 'Zehra', 'Tokat'),
            (2, 'Can', 'Erzincan'),
            (3, 'Arda', 'Samsun') ]
#Kayıtlar listesini tabloya ekle.
imlec.executemany('INSERT INTO musteri VALUES (?,?,?)', kayitlar)
#tabloya yeni kayıtlar eklendi
imlec.execute("INSERT INTO musteri values" " (4, 'Bade', 'Tokat')")
imlec.execute("INSERT INTO musteri values"
" (5, 'Berat', 'Sakarya')")
bgln.commit() #veri tabanı güncellendi
#bir döngü içerisinde tüm kayıtları ada göre listele
print("personel.db içindeki müşteriler Ad'a göre listelendi.")
for kyt in imlec.execute('SELECT * FROM musteri ORDER BY ad'):
    print(kyt)
bgln.close() #veri tabanını kapatır