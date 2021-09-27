'''
Örnek 18.5:
MongoDB ile ‘backup’ isimli bir veri tabanı oluşturup, rehber isimli koleksiyona
(tabloya) yeni kayıtlar ekleyen ve bu kayıtları ekranda gösteren programı
kodlayınız.
'''
from pymongo import MongoClient
""" MongoDB veri tabanına kayıt ekleme"""
try:
    c = MongoClient('mongodb://localhost:27017/')
    #Alternatifi: c = Connection(host="localhost", port=27017)
    print ("veri tabanına bağlanıldı")
except:
    print ("MongoDB bağlantısı başarısız ")

vt = c["backup"]        #veritabanı adı: backup
tablo = vt['rehber']    #tablo adı: rehber
#rehber koleksiyonundaki (tablosundaki) kayıtlar
kayitlar = [
{ "ad": "ada", "adres": "Tokat"},
{ "ad": "ali", "adres": "Mersin"},
{ "ad": "mete", "adres": "Van"},
{ "ad": "Veli", "adres": "Sakarya"}
]
tablo.insert_many(kayitlar) #kayıtlar tabloya eklendi
print ("kayıt eklendi", kayitlar)